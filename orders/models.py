from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from catalog.models import Product

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # No need to manually add '_id'
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=50,
        choices=[("Pending", "Pending"), ("Completed", "Completed")]
    )
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    id = models.IntegerField(max_length=10, primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


