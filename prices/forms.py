from django import forms
from . import models


class PriceForm(forms.ModelForm):

    class Meta:
        model = models.Price
        fields = ['category', 'value']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'value': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'category': 'Categoria',
            'value': 'Valor',
        }
