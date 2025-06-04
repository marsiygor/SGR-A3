import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . import metrics


@login_required(login_url='login')
def home(request):
    waste_record_metrics = metrics.get_waste_and_record_metrics()
    entry_exit_data = metrics.get_entry_exit_data()
    
    # Chart data for clickable cards
    waste_by_category_data = metrics.get_waste_by_category_data()
    waste_by_sector_data = metrics.get_waste_by_sector_data()
    stock_by_category_data = metrics.get_stock_by_category_data()
    stock_by_sector_data = metrics.get_stock_by_sector_data()
    value_by_category_data = metrics.get_value_by_category_data()
    
    context = {
        'waste_record_metrics': waste_record_metrics,
        'entry_exit_data': json.dumps(entry_exit_data),
        'waste_by_category_data': json.dumps(waste_by_category_data),
        'waste_by_sector_data': json.dumps(waste_by_sector_data),
        'stock_by_category_data': json.dumps(stock_by_category_data),
        'stock_by_sector_data': json.dumps(stock_by_sector_data),
        'value_by_category_data': json.dumps(value_by_category_data),
    }
    return render(request, 'home.html', context)
