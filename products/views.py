from django.shortcuts import render
from rest_framework import generics
from products.serializers import ProductDetailSerializer, ProductsListSerializer
from products.models import Product


# Create your views here.
class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductDetailSerializer


class ProductsListView(generics.ListAPIView):
    serializer_class = ProductsListSerializer
    queryset = Product.objects.all()


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()