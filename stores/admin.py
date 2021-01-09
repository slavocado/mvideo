from django.contrib import admin

from .models import Store, Quantity

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'subway', 'work_hours')
    list_filter = ('subway',)
    search_fields = ('address',)

class QuantityAdmin(admin.ModelAdmin):
    list_display = ('product', 'store', 'quantity')
    list_filter = ('store',)

admin.site.register(Store, StoreAdmin)
admin.site.register(Quantity, QuantityAdmin)
