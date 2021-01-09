from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class Specification(models.Model):
    name = models.TextField('Product specification')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('name', max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    specification = models.ForeignKey(Specification, on_delete=models.PROTECT)
    link_to_photos = models.URLField('link', max_length=200)
    short_description = models.TextField('Short description')

    def __str__(self):
        return self.name


class Rating(models.Model):
    quality = models.IntegerField()
    functionality = models.IntegerField()


class Review(models.Model):
    text = models.TextField('Review text')
    recommendation = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
