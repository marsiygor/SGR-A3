from django.db.models import Sum, F
from django.utils.formats import number_format
from django.utils import timezone
from brands.models import Brand
from categories.models import Category
from products.models import Product
from outflows.models import Outflow


def get_product_metrics():
    products = Product.objects.all()
    total_cost_price = sum(product.cost_price * product.quantity for product in products)
    total_selling_price = sum(product.selling_price * product.quantity for product in products)
    total_quantity = sum(product.quantity for product in products)
    total_profit = total_selling_price - total_cost_price

    return dict(
        total_cost_price=number_format(total_cost_price, decimal_pos=2, force_grouping=True),
        total_selling_price=number_format(total_selling_price, decimal_pos=2, force_grouping=True),
        total_quantity=total_quantity,
        total_profit=number_format(total_profit, decimal_pos=2, force_grouping=True),
    )


def get_sales_metrics():
    total_sales = Outflow.objects.count()
    total_products_sold = Outflow.objects.aggregate(total_products_sold=Sum('quantity'))['total_products_sold'] or 0
    total_sales_value = sum(outflow.quantity * outflow.product.selling_price for outflow in Outflow.objects.all())
    total_sales_cost = sum(outflow.quantity * outflow.product.cost_price for outflow in Outflow.objects.all())
    total_sales_profit = total_sales_value - total_sales_cost

    return dict(
        total_sales=total_sales,
        total_products_sold=total_products_sold,
        total_sales_value=number_format(total_sales_value, decimal_pos=2, force_grouping=True),
        total_sales_profit=number_format(total_sales_profit, decimal_pos=2, force_grouping=True),
    )


def get_daily_sales_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    values = list()

    for date in dates:
        sales_total = Outflow.objects.filter(
            created_at__date=date
        ).aggregate(
            total_sales=Sum(F('product__selling_price') * F('quantity'))
        )['total_sales'] or 0
        values.append(float(sales_total))

    return dict(
        dates=dates,
        values=values,
    )


def get_daily_sales_quantity_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    quantities = list()

    for date in dates:
        sales_quantity = Outflow.objects.filter(created_at__date=date).count()
        quantities.append(sales_quantity)

    return dict(
        dates=dates,
        values=quantities,
    )


def get_graphic_product_category_metric():
    categories = Category.objects.all()
    return {category.name: Product.objects.filter(category=category).count() for category in categories}


def get_graphic_product_brand_metric():
    brands = Brand.objects.all()
    return {brand.name: Product.objects.filter(brand=brand).count() for brand in brands}


def get_waste_and_record_metrics():
    from sectors.models import Sector
    from wastes.models import Waste
    from records.models import Record
    from django.db.models import Sum
    
    num_sectors = Sector.objects.count()
    num_wastes = Waste.objects.count()
    total_waste_weight = Waste.objects.aggregate(total=Sum('weight'))['total'] or 0
    
    total_entry_value = Record.objects.filter(is_entry=True).aggregate(total=Sum('value'))['total'] or 0
    total_exit_value = Record.objects.filter(is_entry=False).aggregate(total=Sum('value'))['total'] or 0
    
    return {
        'num_sectors': num_sectors,
        'num_wastes': num_wastes,
        'total_waste_weight': total_waste_weight,
        'total_entry_value': total_entry_value,
        'total_exit_value': total_exit_value,
    }


def get_entry_exit_data():
    from records.models import Record
    from django.utils import timezone
    from django.db.models import Sum
    today = timezone.now().date()
    dates = [today - timezone.timedelta(days=i) for i in range(6, -1, -1)]
    labels = [d.strftime('%d/%m') for d in dates]
    entry_values = []
    exit_values = []
    for d in dates:
        entry = Record.objects.filter(is_entry=True, date__date=d).aggregate(total=Sum('value'))['total'] or 0
        exit = Record.objects.filter(is_entry=False, date__date=d).aggregate(total=Sum('value'))['total'] or 0
        entry_values.append(float(entry))
        exit_values.append(float(exit))
    return {
        'dates': labels,
        'entry_values': entry_values,
        'exit_values': exit_values,
    }
