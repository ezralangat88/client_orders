from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from .models import Customer, Order

class CustomerOrderTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name='Test User', code='123')

    def test_order_creation(self):
        order = Order.objects.create(customer=self.customer, item='Item 1', amount=100)
        self.assertEqual(order.customer, self.customer)
