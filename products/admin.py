from django.contrib import admin

from .models import Category, Product, Specification, Rating, Review

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'link_to_photos', 'short_description')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')

class RatingAdmin(admin.ModelAdmin):
    list_display = ('quality', 'functionality')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'recommendation', 'date', 'product', 'rating')


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Specification)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Review, ReviewAdmin)