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