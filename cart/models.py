from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from catalog.models import Product


class Cart(models.Model):
    id = models.IntegerField(max_length=10, primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    id = models.IntegerField(max_length=10, primary_key=True)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    def increase_product(self, amount=1):
        self.quantity += amount
        self.save()

    def decrease_product(self, amount=1):
        if self.quantity > amount:
            self.quantity -= amount
            self.save()
        else:
            self.delete()