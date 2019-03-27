from django.db import models

class Donuts(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.FloatField(default=1.49)
    image = models.URLField()

    def __str__(self):
        return self.name

class Sandwiches(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.FloatField(default=0.00)
    image = models.URLField()

    def __str__(self):
        return self.name


class Drinks(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.FloatField(default=0.00)
    image = models.URLField()

    def __str__(self):
        return self.name


