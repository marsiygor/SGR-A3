from django.db import models


class Sector(models.Model):
    name = models.CharField(max_length=500)
    responsible = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
