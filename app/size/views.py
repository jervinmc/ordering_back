from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Size
from .serializers import SizeSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from users.serializers import UserSerializer
from color.serializers import ColorSerializer
from color.serializers import Color
from decouple import config
import pusher
class SizeView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Size.objects.all()
    serializer_class=SizeSerializer



class SizeProductID(generics.GenericAPIView):
    def get(self,request,format=None,product_id=None):
        try:
            size = Size.objects.filter(product_id=product_id)
            serializers = SizeSerializer(size,many=True)
            return Response(data=serializers.data)
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])



class SizeEditProduct(generics.GenericAPIView):
    def post(self,request,format=None,product_id=None):
        try:
            res =request.data
            size = Size.objects.filter(product_id=res.get('product_id')).delete()
            color = Color.objects.filter(product_id=res.get('product_id')).delete()
            print(res.get('size_label'))
            size_label = res.get('size_label')
            size_price = res.get('size_price')
            color_label = res.get('color_label')
            for (x,i) in enumerate(size_label):
                if(size_price[x]!=''):
                    serializers_size = SizeSerializer(data={"product_id":res.get('product_id'),"price":size_price[x],"label":i})
                    serializers_size.is_valid(raise_exception=True)
                    serializers_size.save()  
            for (x,i) in enumerate(color_label):
                if(color_label[x]!=''):
                    serializers_color = ColorSerializer(data={"product_id":res.get('product_id'),"label":color_label[x]})
                    serializers_color.is_valid(raise_exception=True)
                    serializers_color.save()
            return Response(data=serializers_size.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])