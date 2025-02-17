from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from catalog.models import Order

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associació amb l'usuari
    card_number = models.CharField(max_length=16)  # Número de la targeta
    expiration_date = models.DateField()  # Data de caducitat
    cvc = models.CharField(max_length=3)  # Codi de seguretat
    payment_status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')])
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)  # Enllaç amb la comanda

    def __str__(self):
        return f"Payment {self.pk} - {self.payment_status}"
