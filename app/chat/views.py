from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Chat
from .serializers import ChatSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from users.serializers import UserSerializer
import pusher
pusher_client = pusher.Pusher(
  app_id='1336209',
  key='33efacb6a0d9c7baad00',
  secret='85da601a0c9bbc86fefa',
  cluster='ap1',
  ssl=True
)
class ChatView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Chat.objects.all()
    serializer_class=ChatSerializer
    def list(self,request,format=None,email=None):
        try:
            if self.request.user.account_type=='Seller':
                print('seller')
                items = Chat.objects.filter(seller_id=self.request.user.id)
                items = ChatSerializer(items,many=True)
                for x in items.data:
                    user = User.objects.filter(id=x['customer_id'])
                    user = UserSerializer(user,many=True)
                    x['users']=user.data[0]
            elif self.request.user.account_type=='Customer':
                print('customer')
                items = Chat.objects.filter(customer_id=self.request.user.id)
                items = ChatSerializer(items,many=True)
                for x in items.data:
                    user = User.objects.filter(id=x['seller_id'])
                    user = UserSerializer(user,many=True)
                    x['users']=user.data[0]
            return Response(status=status.HTTP_200_OK,data=items.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])

class ChatGet(generics.GenericAPIView):
    queryset=Chat.objects.all()
    serializer_class=ChatSerializer
    permission_classes=[permissions.AllowAny]
    def post(self,request):
        items = Chat.objects.filter(channel=request.data.get('channel'))
        items = ChatSerializer(items,many=True)
        return Response(data=items.data)

