from django.db import models
from products.models import Product
from suppliers.models import Supplier


class Inflow(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='inflows')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inflows')
    quantity = models.IntegerField()
    barcode = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.product)

