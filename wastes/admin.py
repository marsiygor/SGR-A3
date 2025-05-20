from django.contrib import admin
from .models import Waste

@admin.register(Waste)
class WasteAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'weight', 'sector', 'created_at')
    list_filter = ('category', 'sector', 'created_at')
    search_fields = ('name', 'category__name', 'description', 'sector__name')
