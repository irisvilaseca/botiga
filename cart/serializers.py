from rest_framework import serializers
from .models import Cart, CartItem
from botiga.catalog.models import Product


class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source="product.name")
    product_price = serializers.ReadOnlyField(source="product.price")

    class Meta:
        model = CartItem
        fields = ['id', 'cart_id', 'product', 'product_id', 'quantity']


class AddToCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)


class UpdateCartSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=1)
