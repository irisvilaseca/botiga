from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product


class Cart(models.Model):
    id = models.AutoField(primary_key=True)  # ✅ Fix: Auto-increment primary key
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.username}"


class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    def increase_product(self, amount=1):
        """Increase product quantity in cart"""
        self.quantity += amount
        self.save()

    def decrease_product(self, amount=1):
        """Decrease product quantity, delete if zero"""
        if self.quantity > amount:
            self.quantity -= amount
            self.save()
        else:
            self.delete()
