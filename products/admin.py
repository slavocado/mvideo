from django.contrib import admin

from .models import Categories, Products, Specification, Ratings, Reviews

admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Specification)
admin.site.register(Ratings)
admin.site.register(Reviews)