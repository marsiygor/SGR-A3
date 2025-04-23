from django import forms
from . import models


class InflowForm(forms.ModelForm):
    barcode = forms.CharField(label='Código de barras', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = models.Inflow
        fields = ['supplier', 'product', 'quantity', 'barcode', 'description']
        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'barcode': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'supplier': 'Fornecedor',
            'product': 'Produto',
            'barcode': 'Código de barras',
            'quantity': 'Quantidade',
            'description': 'Descrição',
        }
