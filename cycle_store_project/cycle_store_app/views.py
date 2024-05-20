# from django.shortcuts import render

# cycle_store_app/views.py

from rest_framework import viewsets
from .models import Vehicle, Customer, CustomerOrder
from .serializers import VehicleSerializer, CustomerSerializer, CustomerOrderSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerOrderViewSet(viewsets.ModelViewSet):
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSerializer

