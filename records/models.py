from django.db import models


class Record(models.Model):
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE, related_name='records')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='records', null=True, blank=True)
    waste = models.ForeignKey('wastes.Waste', on_delete=models.CASCADE, related_name='records', null=True, blank=True)
    unit_price = models.DecimalField(max_digits=20, decimal_places=2, default=0)  # Preço unitário por kg
    value = models.DecimalField(max_digits=20, decimal_places=2)  # Valor total
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_entry = models.BooleanField(default=True)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        if self.waste:
            return f"{self.waste.name} - {self.weight}kg - {'Entrada' if self.is_entry else 'Saída'}"
        return f"{self.category} - R$ {self.value}"
