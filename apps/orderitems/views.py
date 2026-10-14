from django.shortcuts import render

from .models import OrderItem
from rest_framework import viewsets
from .serializer import  OrderItemSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer  
