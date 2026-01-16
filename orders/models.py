import uuid
import random
import string
from django.db import models
from django.conf import settings
from catalogue.models import ProductVariant

def generate_transaction_id():
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=12))

class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    transaction_id = models.CharField(max_length=12, unique=True, default=generate_transaction_id)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    mobile_money_reference = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Order {self.transaction_id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    variant = models.ForeignKey(ProductVariant, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.variant} x {self.quantity}"
