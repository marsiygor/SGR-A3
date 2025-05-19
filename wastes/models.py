from django.db import models


class Waste(models.Model):
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE, related_name='wastes')
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    sector = models.ForeignKey('sectors.Sector', on_delete=models.CASCADE, related_name='wastes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.category} - {self.weight}kg"
