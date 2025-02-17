# payment/serializers.py

from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    order=serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Payment
        fields = ['id', 'user', 'card_number', 'expiration_date', 'cvc', 'payment_status', 'order']
