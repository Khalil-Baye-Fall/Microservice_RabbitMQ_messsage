from math import prod
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import ProductSerializer
# Create your views here.

class ProductView(APIView):
    def post(self, request):
        products = ProductSerializer(data=request.data)
        if products.is_valid():
            products.save()
            return Response(products.data, status=status.HTTP_201_CREATED)
        return Response(products.errors, status=status.HTTP_400_BAD_REQUEST)  
            
    
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
class ProductIdView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return HttpResponse('Data not found')
        
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return HttpResponse('Data not found')
        
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return HttpResponse('Data not found')
        
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


