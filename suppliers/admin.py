from django.contrib import admin
from . import models


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'trade', 'email', 'address', 'neighborhood', 'city',
                    'state', 'country', 'zipcode', 'phone', 'fax', 'cnpj', 'description')
    search_fields = ('name','company', 'trade')


admin.site.register(models.Supplier, SupplierAdmin)
