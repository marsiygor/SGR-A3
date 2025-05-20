from django import forms
from .models import Record
from categories.models import Category
from products.models import Product
from django.utils import timezone


class RecordForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    product = forms.ModelChoiceField(
        queryset=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    value = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    weight = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    is_entry = forms.ChoiceField(
        choices=[(True, 'Entrada'), (False, 'Saída')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    date = forms.DateTimeField(
        initial=timezone.now,
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['product'].queryset = Product.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                self.fields['product'].queryset = Product.objects.none()
        elif self.instance.pk and self.instance.category:
            self.fields['product'].queryset = Product.objects.filter(category=self.instance.category)
        else:
            self.fields['product'].queryset = Product.objects.none()

    class Meta:
        model = Record
        fields = ['category', 'product', 'weight', 'value', 'date', 'is_entry']
