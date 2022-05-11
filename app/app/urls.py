from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.urls.conf import include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from users.views import Login,VerifyUser
from product.views import ProductUserID
from notifications.views import NotificationUserID,NotificationSeen
from carts.views import CartsUserID
from transaction.views import TransactionUserID,TransactionGetall
from channel.views import ChannelGetall,ChannelSend
from chat.views import ChatGet
from rest_framework import permissions
from transaction.views import TransactionBulkCheckout,TransactionNotif
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/product/', include('product.urls')),
    path('api/v1/notifications/', include('notifications.urls')),
    path('api/v1/carts/', include('carts.urls')),
    path('api/v1/inventory-report/', include('inventory_report.urls')),
    path('api/v1/transaction/', include('transaction.urls')),
    path('api/v1/chat/', include('chat.urls')),
    path('api/v1/size/', include('size.urls')),
    path('api/v1/taccount/', include('taccount.urls')),
    path('api/v1/channel/', include('channel.urls')),
    path('api/v1/product_id/<str:product_id>/', ProductUserID.as_view(), name='get_user'),
    path('api/v1/cart_user/<str:user_id>/', CartsUserID.as_view(), name='get_user'),
    path('api/v1/notification_seen/<str:user_id>/', NotificationSeen.as_view(), name='get_user'),
    path('api/v1/verify/<str:email>/', VerifyUser.as_view(), name='get_user'),
    path('api/v1/transaction_user/<str:user_id>/', TransactionUserID.as_view(), name='get_user'),
    path('api/v1/transaction_notif/', TransactionNotif.as_view(), name='get_user'),
    path('api/v1/transaction-add-bulk/', TransactionBulkCheckout.as_view(), name='get_user'),
    path('api/v1/notification_user/<str:user_id>/', NotificationUserID.as_view(), name='get_user'),
    path('api/v1/transaction_getall/', TransactionGetall.as_view(), name='get_user'),
    path('api/v1/channel/', TransactionGetall.as_view(), name='get_user'),
    path('api/v1/channel-admin/<str:account_type>/<int:user_id>/', ChannelGetall.as_view(), name='get_user'),
    path('api/v1/chatgetall/', ChatGet.as_view(), name='get_user'),
    path('api/v1/sendMessage/', ChannelSend.as_view(), name='get_user'),
    path('api/v1/login/', Login.as_view(), name='get_user'),
]