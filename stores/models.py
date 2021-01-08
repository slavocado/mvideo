from django.db import models
from products import models as pmodels

class Store(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField('Store address')
    subway = models.CharField(max_length=200)
    work_hours = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Quantity(models.Model):
    quantity = models.IntegerField()
    store = models.ForeignKey(Store, on_delete=models.PROTECT)
    product = models.ForeignKey(pmodels.Product, on_delete=models.PROTECT)

    def __str__(self):
        return self.quantity