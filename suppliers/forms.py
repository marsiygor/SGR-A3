from django import forms
from . import models
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
import re 


class SupplierForm(forms.ModelForm):

    class Meta:
        model = models.Supplier
        fields = ['name', 'company', 'trade',  'email', 'address', 'neighborhood', 'city', 'state', 'country', 'zipcode', 'phone', 'fax', 'cnpj','description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 100}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'maxlength': 300}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 100}),
            'trade': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 100}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'maxlength': 100}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 200}),
            'neighborhood': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 100}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 100}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 50}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 50}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 10}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 15, 'validators': [RegexValidator(regex=r'^\(\d{2}\) \d{4,5}-\d{4}$', message='Telefone deve estar no formato (XX) XXXX-XXXX ou (XX) XXXXX-XXXX')]}),
            'fax': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 15}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 18, 'validators': [RegexValidator(regex=r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$', message='CNPJ deve estar no formato XX.XXX.XXX/XXXX-XX')]}),
        }
        
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
            'company': 'Razão Social',
            'trade': 'Nome Fantasia',
            'email': 'E-mail',
            'address': 'Endereço', 
            'neighborhood': 'Bairro',
            'city': 'Cidade',
            'state': 'Estado',
            'country': 'País',
            'zipcode': 'CEP',
            'phone': 'Telefone',
            'fax': 'Fax',
            'cnpj': 'CNPJ',
            
        }
        
    def clean_name(self):
        data = self.cleaned_data['name']
        if len(data) > 100:
            raise ValidationError("O nome não pode ter mais de 100 caracteres.")
        return data

    def clean_description(self):
        data = self.cleaned_data['description']
        if len(data) > 300:
            raise ValidationError("A descrição não pode ter mais de 300 caracteres.")
        return data

    def clean_company(self):
        data = self.cleaned_data['company']
        if len(data) > 100:
            raise ValidationError("A empresa não pode ter mais de 100 caracteres.")
        return data

    def clean_trade(self):
        data = self.cleaned_data['trade']
        if len(data) > 100:
            raise ValidationError("O ramo não pode ter mais de 100 caracteres.")
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        if len(data) > 100:
            raise ValidationError("O email não pode ter mais de 100 caracteres.")
        return data

    def clean_address(self):
        data = self.cleaned_data['address']
        if len(data) > 200:
            raise ValidationError("O endereço não pode ter mais de 200 caracteres.")
        return data

    def clean_neighborhood(self):
        data = self.cleaned_data['neighborhood']
        if len(data) > 100:
            raise ValidationError("O bairro não pode ter mais de 100 caracteres.")
        return data

    def clean_city(self):
        data = self.cleaned_data['city']
        if len(data) > 100:
            raise ValidationError("A cidade não pode ter mais de 100 caracteres.")
        return data

    def clean_state(self):
        data = self.cleaned_data['state']
        if len(data) > 50:
            raise ValidationError("O estado não pode ter mais de 50 caracteres.")
        return data

    def clean_country(self):
        data = self.cleaned_data['country']
        if len(data) > 50:
            raise ValidationError("O país não pode ter mais de 50 caracteres.")
        return data

    def clean_zipcode(self):
        data = self.cleaned_data['zipcode']
        if len(data) > 10:
            raise ValidationError("O CEP não pode ter mais de 10 caracteres.")
        return data

    def clean_phone(self):
        data = self.cleaned_data['phone']
        if len(data) > 15:
            raise ValidationError("O telefone não pode ter mais de 15 caracteres.")
        return data

    def clean_fax(self):
        data = self.cleaned_data['fax']
        if len(data) > 15:
            raise ValidationError("O fax não pode ter mais de 15 caracteres.")
        return data

    def clean_cnpj(self):
        data = self.cleaned_data['cnpj']
        if len(data) > 18:
            raise ValidationError("O CNPJ não pode ter mais de 18 caracteres.")
        return data
