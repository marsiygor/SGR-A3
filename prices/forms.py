from django import forms
from . import models
from wastes.models import Waste


class PriceForm(forms.ModelForm):
    waste = forms.ModelChoiceField(queryset=None, widget=forms.Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['waste'].queryset = Waste.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                self.fields['waste'].queryset = Waste.objects.none()
        elif self.instance.pk:
            self.fields['waste'].queryset = Waste.objects.filter(category=self.instance.category)
        else:
            self.fields['waste'].queryset = Waste.objects.none()

    class Meta:
        model = models.Price
        fields = ['category', 'waste', 'value']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'value': forms.NumberInput(attrs={'class': 'form-control'}),
            'waste': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'category': 'Categoria',
            'value': 'Valor',
            'waste': 'Resíduo',
        }
