from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Carts
from .serializers import CartsSerializer
from rest_framework import filters
from rest_framework import status, viewsets
from rest_framework.response import Response
from product.models import Product
from django.db.models import F
from product.serializers import ProductSerializer
class CartsView(viewsets.ModelViewSet):  
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Carts.objects.all()
    serializer_class=CartsSerializer
    
    def create(self,request):
        res = request.data
        item_val = Carts.objects.filter(user_id = res.get('user_id'),product_id = res.get('product_id')).count()
        if(item_val>0):
            Carts.objects.filter(user_id = res.get('user_id'),product_id = res.get('product_id')).update(quantity = F('quantity') + res.get('quantity'))
        else:
            print("okay")
            ser = CartsSerializer(data=res)
            ser.is_valid(raise_exception=True)
            ser.save()
        return Response()



class CartsUserID(generics.GenericAPIView):
    def get(self,request,format=None,user_id=None):
        try:
            items = Carts.objects.filter(user_id=user_id)
            listitem = []
            serializers = CartsSerializer(items,many=True)
            # for x in serializers.data:
            #     print(x['product_id'])
            #     item = Product.objects.filter(id=x['product_id'])
            #     item = ProductSerializer(item,many=True)
            #     x['price'] = item.data[0]['price']
            #     print(x['price'])
            return Response(data=serializers.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])
