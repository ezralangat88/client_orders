from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer

import africastalking
from django.conf import settings

from .models import Order

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()  # Ensure you import Order model
    serializer_class = OrderSerializer
    
    def perform_create(self, serializer):
        order = serializer.save()
        customer = order.customer
        send_sms(customer.phone_number, f"Order {order.item} has been placed.")

