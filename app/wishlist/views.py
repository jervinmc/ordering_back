from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Wishlist
from .serializers import WishlistSerializer
from rest_framework import filters
from rest_framework import status, viewsets
from rest_framework.response import Response
from product.models import Product
from django.db.models import F
from product.serializers import ProductSerializer
class WishlistView(viewsets.ModelViewSet):  
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Wishlist.objects.all()
    serializer_class=WishlistSerializer
    
    def create(self,request):
        res = request.data
        item_val = Wishlist.objects.filter(user_id = res.get('user_id'),product_id = res.get('product_id')).count()
        if(item_val>0):
            Wishlist.objects.filter(user_id = res.get('user_id'),product_id = res.get('product_id')).update(quantity = F('quantity') + res.get('quantity'))
        else:
            print("okay")
            ser = WishlistSerializer(data=res)
            ser.is_valid(raise_exception=True)
            ser.save()
        return Response()



class WishlistUserID(generics.GenericAPIView):
    def get(self,request,format=None,user_id=None):
        try:
            items = Wishlist.objects.filter(user_id=user_id)
            listitem = []
            serializers = WishlistSerializer(items,many=True)
            for x in serializers.data:
                print(x['product_id'])
                item = Product.objects.filter(id=x['product_id'])
                item = ProductSerializer(item,many=True)
                x['price'] = item.data[0]['price']
                x['stocks'] = item.data[0]['stocks']
                x['descriptions'] = item.data[0]['descriptions']
                print(x['price'])
            return Response(data=serializers.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])
