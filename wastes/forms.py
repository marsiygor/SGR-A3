from django import forms
from .models import Waste
from categories.models import Category
from sectors.models import Sector


class WasteForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
        label='Nome do resíduo'
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    sector = forms.ModelChoiceField(
        queryset=Sector.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    weight = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        required=False
    )

    class Meta:
        model = Waste
        fields = ['name', 'category', 'weight', 'description', 'sector']
