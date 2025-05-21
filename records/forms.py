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
    # Campo oculto para armazenar o preço por kg, que será preenchido automaticamente
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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Se o registro já existe e tem um resíduo associado, preencher o preço unitário
        if self.instance.pk and self.instance.waste:
            self.fields['unit_price'].initial = self.instance.waste.price_per_kg
        
        # Verificar se estamos atualizando os dados com um novo resíduo
        if 'waste' in self.data and self.data.get('waste'):
            try:
                waste_id = int(self.data.get('waste'))
                waste = Waste.objects.get(id=waste_id)
                # Sempre use o preço do resíduo
                self.data._mutable = True
                self.data['unit_price'] = waste.price_per_kg
                self.data._mutable = False
            except (ValueError, TypeError, Waste.DoesNotExist):
                pass

    class Meta:
        model = Record
        fields = ['waste', 'weight', 'unit_price', 'is_entry', 'date']
        # unit_price está na lista para ser incluído no processamento, mas não aparecerá na interface do usuário

    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # Obter a categoria automaticamente do resíduo
        if instance.waste:
            instance.category = instance.waste.category
            
            # Sempre usar o preço do resíduo
            instance.unit_price = instance.waste.price_per_kg
            
            # Calcular o valor total com base no peso e no preço do resíduo
            instance.value = instance.weight * instance.unit_price
        
        if commit:
            instance.save()
        return instance
