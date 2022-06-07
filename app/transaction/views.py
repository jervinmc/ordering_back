from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework import filters
from product.models import Product
from product.serializers import ProductSerializer
from rest_framework import status, viewsets
from carts.models import Carts
from inventory_report.models import InventoryReport
from rest_framework.response import Response
from product.models import Product
from django.db.models import F
from notifications.models import Notification
from notifications.serializers import NotificationSerializer
from inventory_report.serializers import InventoryReportSerializer
from taccount.serializers import TaccountSerializer
from taccount.models import Taccount
import http.client
import json
import pusher
from datetime import datetime
now = datetime.now()
from decouple import config
pusher_client = pusher.Pusher(
  app_id=config('pusher_id'),
  key=config('pusher_key'),
  secret=config('secret_key'),
  cluster='ap1',
  ssl=True
)
class TransactionView(viewsets.ModelViewSet):  
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Transaction.objects.all()
    serializer_class=TransactionSerializer

    def create(self,request):
        res = request.data
        print(res)
        print()
        serializer = TransactionSerializer(data=res)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        Product.objects.filter(id=res.get('product_id')).update(stocks=F('stocks')-res.get('quantity'))
        Product.objects.filter(id=res.get('product_id')).update(numBuy=F('numBuy')+res.get('quantity'))
        serializers = NotificationSerializer(data={"user_id":1,"descriptions":f"You have a new order({res.get('product_name')}) from user_id {res.get('user_id')}","image":res.get('image'),"viewed":"no","module":"transactions","users_profile":res.get('users_profile')})
        serializers.is_valid(raise_exception=True)
        serializers.save()
        item_inv = Product.objects.filter(id=res.get('product_id'))
        serializer = ProductSerializer(item_inv,many=True)
        if(serializer.data[0]['stocks']<5):
            item1 = NotificationSerializer(data={"user_id":1,"descriptions":f"Running out of stocks product: {res.get('product_id')}","image":res.get('image'),"users_profile":res.get('users_profile'),"module":'products'})
            item1.is_valid(raise_exception=True)
            item1.save()
        inventory_serializer = InventoryReportSerializer(data={"product_name":res.get('product_name'),"status":"Subtract","stocks":res.get('quantity'),'remaining_stocks':serializer.data[0]['stocks']})
        inventory_serializer.is_valid(raise_exception=True)
        inventory_serializer.save()
        pusher_client.trigger('notification_admin', 'my-test', {'message': f'Item status : {res.get("status")}','user_id':res.get("user_id")})
        return Response()
    
class TransactionBulkCheckout(generics.GenericAPIView):
    def post(self,request):
        res = request.data
        print(res['data'])
        for x in res['data']:
            print("okay")
            x['status'] = 'Pending'
            x['username'] = res.get('username')
            x['barangay'] = res.get('barangay')
            x['address'] = res.get('address')
            x['fullname'] = res.get('fullname')
            x['date'] = res.get('date')
            x['users_profile'] = res.get('users_profile')
            x['city'] = res.get('city')
            x['zip'] = res.get('zip')
            x['province'] = res.get('province')
            print(x)
            x['subtotal']= float(x['price'])+15.00
            Taccount.objects.create(account="Product Sold",debit=x['subtotal'],credit=0,date=now)
            x['contact_number']=res.get('contact_number')
            serializers = TransactionSerializer(data=x)
            serializers.is_valid(raise_exception=True)
            serializers.save()
            print("okay")
            item_inv = Product.objects.filter(id=x['product_id'])
            serializer = ProductSerializer(item_inv,many=True)
            if(serializer.data[0]['stocks']<5):
                item1 = NotificationSerializer(data={"user_id":1,"descriptions":f"Running out of stocks product: {x['product_id']}","image":x['image'],"users_profile":x['users_profile']})
                item1.is_valid(raise_exception=True)
                item1.save()
            inventory_serializer = InventoryReportSerializer(data={"product_name":res.get('product_name'),"status":"Subtract","stocks":x['quantity'],"remaining_stocks":serializer.data[0]['stocks'],"module":"products"})
            Carts.objects.filter(user_id = res['data'][0]['user_id'],product_id=x['product_id'] ).delete()
            # Product.objects.filter(id=x['product_id']).update(stocks=F('stocks')-x['quantity'])
            # Product.objects.filter(id=res.get('product_id')).update(numBuy=F('numBuy')+res.get('quantity'))
            NotificationSerializer(data={"user_id":1,"descriptions":f"You have a new order({x['product_name']}) from user_id = {res.get('user_id')}","image":x['image'],"module":"transactions"})
        pusher_client.trigger('notification_admin', 'my-test', {'message': f'Item status : {res.get("status")}','user_id':res.get("user_id"),"viewed":"no"})
        print(res['data'][0]['user_id'])
        print("okayyyyy")
        # Carts.objects.filter(user_id = res['data'][0]['user_id']).delete()
        return Response()

class TransactionUserID(generics.GenericAPIView):
    def get(self,request,format=None,user_id=None):
        try:
            items = Transaction.objects.filter(user_id=user_id)
            listitem = []
            serializers = TransactionSerializer(items,many=True)
     
            for x in serializers.data:
                print(x['product_id'])
                item = Product.objects.filter(id=x['product_id'])
                item = ProductSerializer(item,many=True)
                if(item.data!=[]):
                    # print(item.data[0])
                    print("FGAREGAEGE")
                    x['price'] = item.data[0]['price']
                    x['product_name'] = item.data[0]['product_name']
                    print(item.data[0]['product_name'])
                    print(x['price'])
            return Response(data=serializers.data)    
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])


class TransactionNotif(generics.GenericAPIView):
    def post(self,request):
        res = request.data
        try:
            conn = http.client.HTTPSConnection("api.itexmo.com")
            payload = json.dumps({
            "Email": "jmacalawapersonal@gmail.com",
            "Password": "wew123WEW ",
            "Recipients": [
                f"{res.get('contact_number')}"
            ],
            "Message": "Your item is now accepted.",
            "ApiCode": "TR-JERVI771273_W0L8V",
            "SenderId": "ITEXMO SMS"
            })
            headers = {
            'Content-Type': 'application/json'
            }
            conn.request("POST", "/api/broadcast", payload, headers)
            res = conn.getresponse()
            data = res.read()
            print(data.decode("utf-8"))
            serializers = NotificationSerializer(data={"user_id":res.get('user_id'),"descriptions":res.get('descriptions'),"image":res.get('image'),"viewed":"no"})
            serializers.is_valid(raise_exception=True)
            serializers.save()
            pusher_client.trigger('notif', 'my-test', {'message': f'Item status : {res.get("status")}','user_id':res.get("user_id")})
        except Exception as e:
            print(e)
        return Response()

class TransactionGetall(generics.GenericAPIView):
    def get(self,request,format=None):
        try:
            items = Transaction.objects.all()
            listitem = []
            serializers = TransactionSerializer(items,many=True)
            print(serializers.data)
            print("OKAYYYYYYFAWERCAEWRAEFADF")
            for x in serializers.data:
                print(x['product_id'])
                item = Product.objects.filter(id=x['product_id'])
                item = ProductSerializer(item,many=True)
                if(len(item.data)==0):
                    pass
                else:
                    x['price'] = item.data[0]['price']
                    x['product_name'] = item.data[0]['product_name']
                    print(item.data[0]['product_name'])
                    print(x['price'])
            return Response(data=serializers.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])


