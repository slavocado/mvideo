from django.contrib import admin
from .models import Category, Product, Specification, Rating, Review

from import_export.admin import ImportExportActionModelAdmin


@admin.register(Product)
class ProductAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'category', 'link_to_photos', 'short_description')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')


@admin.register(Rating)
class RatingAdmin(ImportExportActionModelAdmin):
    list_display = ('quality', 'functionality')


@admin.register(Review)
class ReviewAdmin(ImportExportActionModelAdmin):
    list_display = ('text', 'recommendation', 'date', 'product', 'rating')


admin.site.register(Category)
admin.site.register(Specification)