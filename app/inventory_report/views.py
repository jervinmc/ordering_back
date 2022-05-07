from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import InventoryReport
from .serializers import InventoryReportSerializer
from rest_framework import filters
from rest_framework import status, viewsets
from rest_framework.response import Response
class InventoryReportView(viewsets.ModelViewSet):  
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=InventoryReport.objects.all()
    serializer_class=InventoryReportSerializer



class InventoryReportUserID(generics.GenericAPIView):
    def get(self,request,format=None,InventoryReport_id=None):
        try:
            InventoryReport = InventoryReport.objects.filter(user_id=InventoryReport_id)
            serializers = InventoryReportSerializer(InventoryReport,many=True)
            print(serializers.data)
            return Response(data=serializers.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])
