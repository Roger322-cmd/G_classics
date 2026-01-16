from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order, OrderItem

@receiver(post_save, sender=Order)
def handle_order_paid(sender, instance, created, **kwargs):
    if not created and instance.status == "paid":
        for item in instance.items.select_related("variant"):
            variant = item.variant
            if variant.stock >= item.quantity:
                variant.stock -= item.quantity
                variant.save()
