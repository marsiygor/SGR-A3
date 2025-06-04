from rest_framework import serializers
from .models import Waste


class WasteSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    sector_name = serializers.ReadOnlyField(source='sector.name')
    current_stock = serializers.SerializerMethodField()
    
    class Meta:
        model = Waste
        fields = ['id', 'name', 'category', 'category_name', 'weight', 'price_per_kg', 
                  'description', 'sector', 'sector_name', 'current_stock', 'created_at', 'updated_at']
    
    def get_current_stock(self, obj):
        """Calculate current stock for this waste (entries minus exits)"""
        from records.models import Record
        from django.db.models import Sum
        
        entry_weight = Record.objects.filter(
            waste=obj, 
            is_entry=True
        ).aggregate(total=Sum('weight'))['total'] or 0
        
        exit_weight = Record.objects.filter(
            waste=obj, 
            is_entry=False
        ).aggregate(total=Sum('weight'))['total'] or 0
        
        return float(entry_weight - exit_weight)
