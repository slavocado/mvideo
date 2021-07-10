from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from products.serializers import ProductDetailSerializer, ProductsListSerializer
from products.models import Product
from rest_framework import status
from rest_framework.response import Response


# Create your views here.
class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductDetailSerializer


class ProductsListView(generics.ListAPIView):
    serializer_class = ProductsListSerializer
    queryset = Product.objects.all()


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
    

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)

    except Product.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductDetailSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)