from django.contrib import admin
from .models import Store, Quantity

from import_export.admin import ImportExportActionModelAdmin


def apply_full_stock(modeladmin, request, queryset):
    for quantity in queryset:
        quantity.quantity = 1000
        quantity.save()


apply_full_stock.short_description = 'Apply full stock'


@admin.register(Store)
class StoreAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'address', 'subway', 'work_hours')
    list_filter = ('subway',)
    search_fields = ('address',)


@admin.register(Quantity)
class QuantityAdmin(ImportExportActionModelAdmin):
    list_display = ('product', 'store', 'quantity')
    list_filter = ('store',)
    actions = [apply_full_stock, ]
