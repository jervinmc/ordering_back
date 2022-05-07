from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework import filters
from rest_framework import status, viewsets
from rest_framework.response import Response
class ProductView(viewsets.ModelViewSet):  
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Product.objects.all()
    serializer_class=ProductSerializer



class ProductUserID(generics.GenericAPIView):
    def get(self,request,format=None,product_id=None):
        try:
            product = Product.objects.filter(user_id=product_id)
            serializers = ProductSerializer(product,many=True)
            print(serializers.data)
            return Response(data=serializers.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])
