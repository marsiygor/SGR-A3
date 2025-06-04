from django import forms
from .models import Record
from wastes.models import Waste
from django.utils import timezone


class RecordForm(forms.ModelForm):
    waste = forms.ModelChoiceField(
        queryset=Waste.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_waste'}),
        label='Resíduo'
    )
    weight = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_weight'}),
        label='Peso (kg)'
    )
    unit_price = forms.DecimalField(
        widget=forms.HiddenInput(attrs={'id': 'id_unit_price'}),
        required=False
    )
    is_entry = forms.ChoiceField(
        choices=[(True, 'Entrada'), (False, 'Saída')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Tipo'
    )
    date = forms.DateTimeField(
        initial=timezone.now,
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        label='Data e Hora'
    )

    def clean(self):
        cleaned_data = super().clean()
        waste = cleaned_data.get('waste')
        weight = cleaned_data.get('weight')
        is_entry = cleaned_data.get('is_entry')
        
        # Convert string to boolean if necessary
        if isinstance(is_entry, str):
            is_entry = is_entry == 'True'
        
        # Check stock availability for exits
        if not is_entry and waste and weight:
            from django.db.models import Sum
            
            # Calculate current stock for this specific waste
            entry_weight = Record.objects.filter(
                waste=waste, 
                is_entry=True
            ).aggregate(total=Sum('weight'))['total'] or 0
            
            exit_weight = Record.objects.filter(
                waste=waste, 
                is_entry=False
            ).aggregate(total=Sum('weight'))['total'] or 0
            
            # If editing existing record, exclude it from calculations
            if self.instance.pk:
                if self.instance.is_entry:
                    entry_weight -= self.instance.weight
                else:
                    exit_weight -= self.instance.weight
            
            current_stock = entry_weight - exit_weight
            
            if weight > current_stock:
                raise forms.ValidationError(
                    f'Estoque insuficiente para {waste.name}. '
                    f'Estoque atual: {current_stock:.2f}kg, '
                    f'Tentativa de saída: {weight:.2f}kg'
                )
        
        return cleaned_data

    class Meta:
        model = Record
        fields = ['waste', 'weight', 'unit_price', 'is_entry', 'date']

    def save(self, commit=True):
        instance = super().save(commit=False)
        
        if instance.waste:
            instance.category = instance.waste.category
            instance.unit_price = instance.waste.price_per_kg
            instance.value = instance.weight * instance.unit_price
        
        if commit:
            instance.save()
        return instance
