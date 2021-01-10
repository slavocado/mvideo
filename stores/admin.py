from django.contrib import admin
from .models import Store, Quantity

from import_export.admin import ImportExportActionModelAdmin


@admin.register(Store)
class StoreAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'address', 'subway', 'work_hours')
    list_filter = ('subway',)
    search_fields = ('address',)


@admin.register(Quantity)
class QuantityAdmin(ImportExportActionModelAdmin):
    list_display = ('product', 'store', 'quantity')
    list_filter = ('store',)
