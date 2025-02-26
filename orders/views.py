from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from .models import Order
from .serializers import OrderSerializer
from cart.models import Cart
from cart.serializers import CartItemSerializer


class OrderViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def order_history(self, request):
        """Retrieve completed orders"""
        orders = Order.objects.filter(user=request.user, status="Completed")
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def unfinished_carts(self, request):
        """Retrieve carts that were not completed"""
        unfinished_carts = Cart.objects.filter(user=request.user, is_active=True)
        serializer = CartItemSerializer(unfinished_carts, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['delete'])
    def delete_unfinished_carts(self, request):
        """Delete abandoned carts"""
        deleted_count, _ = Cart.objects.filter(user=request.user, is_active=True).delete()
        return Response({'message': f'{deleted_count} abandoned carts deleted'}, status=status.HTTP_204_NO_CONTENT)
