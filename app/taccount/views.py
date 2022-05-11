from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Taccount
from .serializers import TaccountSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from users.serializers import UserSerializer
from decouple import config
import pusher
class TaccountView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Taccount.objects.all()
    serializer_class=TaccountSerializer

