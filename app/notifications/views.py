from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework import filters
from rest_framework import status, viewsets
from rest_framework.response import Response
class NotificationView(viewsets.ModelViewSet):  
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Notification.objects.all()
    serializer_class=NotificationSerializer



class NotificationUserID(generics.GenericAPIView):
    def get(self,request,format=None,user_id=None):
        try:
            items = Notification.objects.filter(user_id=user_id)
            serializers = NotificationSerializer(items,many=True)
            print(serializers.data)
            return Response(data=serializers.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])


class NotificationSeen(generics.GenericAPIView):
    def get(self,request,format=None,user_id=None):
        try:
            items = Notification.objects.filter(user_id=user_id).update(viewed='yes')
            # serializers = NotificationSerializer(items,many=True)
            # print(serializers.data)
            return Response(data=[])
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])