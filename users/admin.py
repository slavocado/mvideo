from django.contrib import admin

from .models import User, Favourite, Order

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'age', 'email')
    search_fields = ('name', 'surname')

class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')
    search_fields = ('user',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'product')
    search_fields = ('user',)

admin.site.register(User, UserAdmin)
admin.site.register(Favourite, FavouriteAdmin)
admin.site.register(Order, OrderAdmin)
