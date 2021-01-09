from django.contrib import admin
from django.urls import path, include
from products.views import *


app_name = 'products'
urlpatterns = [
    path('product/create/', ProductCreateView.as_view()),
    path('all/', ProductsListView.as_view()),
    path('product/detail/<int:pk>/', ProductDetailView.as_view()),
]
