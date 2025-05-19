from django.db import models


class Record(models.Model):
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE, related_name='records')
    value = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.category} - R$ {self.value}"
