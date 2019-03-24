from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.FloatField(default=0.00)
    image = models.URLField()

    def __str__(self):
        return self.name
