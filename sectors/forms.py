from django import forms
from .models import Sector


class SectorForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    responsible = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    location = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Sector
        fields = ['name', 'responsible', 'location']
