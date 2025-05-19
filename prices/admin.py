from django.contrib import admin
from . import models


class PriceAdmin(admin.ModelAdmin):
    list_display = ('category', 'value', 'created_at',)
    search_fields = ('category__name',)


admin.site.register(models.Price, PriceAdmin)
