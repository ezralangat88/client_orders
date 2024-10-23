# api/serializers.py
from rest_framework import serializers
from .models import Customer, Order

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'code']  # Specify fields you want to expose in the API

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()  # Nested serializer for customer

    class Meta:
        model = Order
        fields = ['id', 'customer', 'item', 'amount', 'time']  # Fields to expose in the API
