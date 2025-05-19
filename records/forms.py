from django import forms
from .models import Record
from categories.models import Category
from django.utils import timezone


class RecordForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    value = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    date = forms.DateTimeField(
        initial=timezone.now,
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})
    )

    class Meta:
        model = Record
        fields = ['category', 'value', 'date']
