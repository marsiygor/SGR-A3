from rest_framework import serializers
from .models import Waste


class WasteSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    sector_name = serializers.ReadOnlyField(source='sector.name')
    
    class Meta:
        model = Waste
        fields = ['id', 'name', 'category', 'category_name', 'weight', 'price_per_kg', 
                  'description', 'sector', 'sector_name', 'created_at', 'updated_at']
