from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class Specification(models.Model):
    name = models.TextField('Product specification')

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Categories, on_delete=models.PROTECT)
    specification = models.ForeignKey(Specification, on_delete=models.PROTECT)
    link_to_photos = models.URLField(max_length=200)
    short_description = models.TextField('Short description')

    def __str__(self):
        return self.name

class Ratings(models.Model):
    quality = models.IntegerField
    functionality = models.IntegerField

class Reviews(models.Model):
    text = models.TextField('Review text')
    recommendation = models.BooleanField
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Products, on_delete=models.PROTECT)
    rating = models.ForeignKey(Ratings, on_delete=models.CASCADE)

    def __str__(self):
        return self.text