# payment/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Payment
from .serializers import PaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]  # Només usuaris autenticats poden crear pagaments

    def perform_create(self, serializer):
        # Aquí afegim la lògica per associar el pagament amb l'usuari autenticat
        # i la comanda seleccionada.
        user = self.request.user
        order = serializer.validated_data['order']
        payment_status = 'Pending'  # O qualsevol lògica per establir l'estat inicial

        serializer.save(user=user, payment_status=payment_status)
        
        # Pots actualitzar l'històric de comandes aquí, si cal, per exemple:
        # order.payment_status = 'Paid'
        # order.save()
