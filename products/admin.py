from django.contrib import admin

from .models import Category, Product, Specification, Rating, Review

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Specification)
admin.site.register(Rating)
admin.site.register(Review)