from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from .cart import Cart as SessionCart
from .models import Cart, CartItem
from catalogue.models import ProductVariant

@receiver(user_logged_in)
def merge_carts_on_login(sender, user, request, **kwargs):
    session_cart = SessionCart(request)

    # If user has no DB cart, create one
    cart, created = Cart.objects.get_or_create(user=user)

    # Loop through session cart items
    for item in session_cart:
        variant = item["variant"]
        quantity = item["quantity"]

        # Merge or create CartItem
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            variant=variant,
            defaults={"quantity": quantity}
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

    # Clear session cart after merge
    session_cart.clear()
