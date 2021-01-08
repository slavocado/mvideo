from django.contrib import admin

from .models import User, Favourite, Order

admin.site.register(User)
admin.site.register(Favourite)
admin.site.register(Order)
