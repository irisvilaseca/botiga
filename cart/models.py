from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from catalog.models import Product


class Cart(models.Model):
    id = models.IntegerField(max_length=10)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    id = models.IntegerField(max_length=10)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()