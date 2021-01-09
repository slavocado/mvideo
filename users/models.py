from django.db import models
from products import models as pmodels

class User(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Order(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(pmodels.Product, on_delete=models.PROTECT)


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(pmodels.Product, on_delete=models.PROTECT)
