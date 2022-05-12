from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework import filters
from rest_framework import status, viewsets
from rest_framework.response import Response
from size.serializers import SizeSerializer
class ProductView(viewsets.ModelViewSet):  
    filter_backends = [filters.SearchFilter]
    search_fields = ['product_name','price']
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    def create(self,request):
        res = request.data
        print(res)
        serializers = ProductSerializer(data=res)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        size_label = res.get('size_label').split(',')
        size_price = res.get('size_price').split(',')
        # for (x,i) in enumerate(size_label):
        #     serializers_size = SizeSerializer(data={"product_id":serializers.data['id'],"price":size_price[x],"label":i})
        #     serializers_size.is_valid(raise_exception=True)
        #     serializers_size.save()  

        return Response()

class ProductUserID(generics.GenericAPIView):
    def get(self,request,format=None,product_id=None):
        try:
            product = Product.objects.filter(user_id=product_id)
            serializers = ProductSerializer(product,many=True)
            return Response(data=serializers.data)
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])
