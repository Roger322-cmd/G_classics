from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart as SessionCart
from .models import Cart, CartItem
from catalogue.models import ProductVariant


def add_to_cart(request, variant_id):
    variant = get_object_or_404(ProductVariant, id=variant_id)
    quantity = int(request.POST.get("quantity", 1))

    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
        item, created = CartItem.objects.get_or_create(cart=cart, variant=variant)
        if created:
            item.quantity = quantity
        else:
            item.quantity += quantity
        item.save()
    else:
        session_cart = SessionCart(request)
        session_cart.add(variant_id, quantity)

    return redirect("cart:cart_detail")


def remove_from_cart(request, variant_id):
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
        CartItem.objects.filter(cart=cart, variant_id=variant_id).delete()
    else:
        session_cart = SessionCart(request)
        session_cart.remove(variant_id)

    return redirect("cart:cart_detail")


def cart_detail(request):
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
        items = cart.items.select_related("variant", "variant__product")
        total = cart.total_price
        is_persistent = True
    else:
        session_cart = SessionCart(request)
        items = list(session_cart)
        total = session_cart.get_total_price()
        is_persistent = False

    return render(request, "cart/cart_detail.html", {
        "items": items,
        "total": total,
        "is_persistent": is_persistent,
    })
