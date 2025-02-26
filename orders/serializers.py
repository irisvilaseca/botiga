from rest_framework import serializers
from .models import Order
from cart.serializers import CartItemSerializer

class OrderSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(source="cart.items", many=True, read_only=True)

    class OrderSerializer(serializers.ModelSerializer):
        class Meta:
            model = Order
            fields = ['id', 'user', 'total_price', 'status', 'created_at']
