from django import forms
from django.core.exceptions import ValidationError
from . import models


class OutflowForm(forms.ModelForm):
    class Meta:
        model = models.Outflow
        fields = ['product', 'quantity', 'barcode','description']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'barcode': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'product': 'Produto',
            'quantity': 'Quantidade',
            'barcode': 'Código de barras',
            'description': 'Descrição',
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')
        barcode = self.cleaned_data.get('barcode')

        if barcode:
            try:
                barcode_product = models.Product.objects.get(barcode=barcode)
                if barcode_product != product:
                    raise ValidationError(
                        f'O código de barras fornecido não corresponde ao produto selecionado.'
                    )
            except models.Product.DoesNotExist:
                raise ValidationError(
                    f'Não foi encontrado nenhum produto com o código de barras fornecido.'
                )

        if not product.inflows.filter(barcode=barcode).exists():
            raise ValidationError(
                f'O código de barras fornecido não está associado a nenhum inflow do produto {product.title}.'
            ) 

        if quantity > product.quantity:
            raise ValidationError(
                f'A quantidade disponível em estoque para o produto {product.title} é de {product.quantity} unidades.'
            )

        return quantity
