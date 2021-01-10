from django.contrib import admin
from .models import User, Favourite, Order

from import_export.admin import ImportExportActionModelAdmin


@admin.register(User)
class UserAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'surname', 'age', 'email')
    search_fields = ('name', 'surname')


@admin.register(Favourite)
class FavouriteAdmin(ImportExportActionModelAdmin):
    list_display = ('user', 'product')
    search_fields = ('user',)


@admin.register(Order)
class OrderAdmin(ImportExportActionModelAdmin):
    list_display = ('user', 'date', 'product')
    search_fields = ('user',)

