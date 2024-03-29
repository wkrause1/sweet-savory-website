from django.db import models

class Sweet(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.FloatField(default=1.49)
    image = models.URLField()
    offered = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Savory(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.FloatField(default=0.00)
    image = models.URLField()
    offered = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "savories"


class Drink(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.FloatField(default=0.00)
    image = models.URLField()
    offered = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Home(models.Model):
    about_us = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.about_us

    class Meta:
        verbose_name = "Home Page Text"
        verbose_name_plural = "Home Page Text"

