from django.contrib import admin
from .models import Record


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('category', 'value', 'date')
    list_filter = ('category', 'date')
    search_fields = ('category__name',)
