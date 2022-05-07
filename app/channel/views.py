from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Channel
from .serializers import ChannelSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from users.serializers import UserSerializer
from chat.models import Chat
from chat.serializers import ChatSerializer
import pusher
from decouple import config
pusher_client = pusher.Pusher(
  app_id=config('pusher_id'),
  key=config('pusher_key'),
  secret=config('secret_key'),
  cluster='ap1',
  ssl=True
)
class ChannelView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Channel.objects.all()
    serializer_class=ChannelSerializer
    def list(self,request,format=None,account_type=None,user_id=None):
        items = []
        try:
            if account_type=='Seller':
                items = Channel.objects.filter(customer_id=user_id)
                items = ChannelSerializer(items,many=True)
                for x in items.data:
                    user = User.objects.filter(id=x['customer_id'])
                    user = UserSerializer(user,many=True)
                    x['users']=user.data[0]
            return Response(status=status.HTTP_200_OK,data=items.data) 
        except Exception as e:
            print(e)
            return Response(data=[])

class ChannelSend(generics.GenericAPIView):
    queryset=Channel.objects.all()
    serializer_class=ChannelSerializer
    permission_classes=[permissions.AllowAny]
    def post(self,request):
        pusher_client.trigger(request.data.get('channel'), 'my-test', {'message': request.data.get('message')})
        serializer = ChatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response()


class ChannelGetall(generics.GenericAPIView):
    queryset=Channel.objects.all()
    serializer_class=ChannelSerializer
    permission_classes=[permissions.AllowAny]
    def get(self,request,format=None,account_type=None,user_id=None):
        items = []
        try:
            if account_type=='Admin':
                items = Channel.objects.filter(seller_id=user_id)
                items = ChannelSerializer(items,many=True)
                for x in items.data:
                    user = User.objects.filter(id=x['customer_id'])
                    user = UserSerializer(user,many=True)
                    x['users']=user.data[0]
            return Response(status=status.HTTP_200_OK,data=items.data) 
        except Exception as e:
            print(e)
            return Response(data=[])