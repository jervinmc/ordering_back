from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import User
from .serializers import UserSerializer
from rest_framework import filters
from rest_framework import status, viewsets
from channel.models import Channel
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string, get_template
import string
from channel.serializers import ChannelSerializer
import random
import string
from rest_framework.response import Response
class UserView(viewsets.ModelViewSet):  
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
    def create(self,request):
        res = request.data
        serializers = UserSerializer(data=res)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        message = get_template('otp.html').render({"email":request.data.get('email')})
        msg = EmailMultiAlternatives('OTP', message,'naidtngcolo@gmail.com', [request.data.get('email')])
        html_content = f'<p>This is an<strong>important</strong> message.</p>'
        msg.content_subtype = "html"
        msg.send()
        return Response()
        


class Login(generics.GenericAPIView):
    def post(self,request,format=None):
        try:
            res = request.data
            items = User.objects.filter(email=res.get('email'),password=res.get('password')).count()
            if(items>0):
               items = User.objects.filter(email=res.get('email'),password=res.get('password')) 
               items = UserSerializer(items,many=True)
               print(items.data)
               if(items.data[0]['account_type']=='Client'):
                   items_channel = Channel.objects.filter(customer_id=items.data[0]['id']).count()
                   if(items_channel==0):
                        id_gen = id_generator()
                        items_1 = ChannelSerializer(data={"customer_id":items.data[0]['id'],"seller_id":"1","channel":id_gen})
                        items_1.is_valid(raise_exception=True)
                        items_1.save()
                        items.data[0]['channel'] = id_gen
                   else:
                       item_channel = Channel.objects.filter(customer_id=items.data[0]['id'])
                       serializer = ChannelSerializer(item_channel,many=True)
                       items.data[0]['channel'] = serializer.data[0]['channel']
                    
            return Response(status=status.HTTP_200_OK,data=items.data)
            
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])



def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
class VerifyUser(generics.GenericAPIView):
    def get(self,request,format=None,email=None):
        User.objects.filter(email=email).update(status='Activated')
        return Response()


class EditUser(generics.GenericAPIView):
    def post(self,request):
        res = request.data
        items = User.objects.filter(id=res.get('user_id'))
        items = UserSerializer(data=res)
        items.is_valid(raise_exception=True)
        items.save()
        return Response()



class ResetPassword(generics.GenericAPIView):
    def post(self,request):
        res = request.data
        password = id_generator()
        User.objects.filter(email=res.get('email')).update(password=password)
        message = get_template('forgot_pass.html').render({"password":password})
        msg = EmailMultiAlternatives('OTP', message,'naidtngcolo@gmail.com', [request.data.get('email')])
        html_content = f'<p></p>'
        msg.content_subtype = "html"
        msg.send()
        return Response()


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))