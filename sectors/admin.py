from django.contrib import admin
from . import models


class SectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'responsible', 'location',)
    search_fields = ('name', 'responsible',)


admin.site.register(models.Sector, SectorAdmin)
