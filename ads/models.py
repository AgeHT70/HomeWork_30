from django.db import models


class Ads(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10000, decimal_places=2)
    description = models.CharField(max_length=2000)
    address = models.CharField(max_length=250)
    is_published = models.BooleanField(default=False)


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
