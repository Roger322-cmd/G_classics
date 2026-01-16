from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from .models import Order, OrderItem

@login_required
def checkout(request):
    cart = request.user.cart
    if request.method == "POST":
        order = Order.objects.create(
            user=request.user,
            total_amount=cart.total_price,
        )
        for item in cart.items.select_related("variant"):
            OrderItem.objects.create(
                order=order,
                variant=item.variant,
                price=item.variant.final_price,
                quantity=item.quantity,
            )
        cart.items.all().delete()
        return redirect("orders:order_detail", transaction_id=order.transaction_id)

    return render(request, "orders/checkout.html", {"cart": cart})


@login_required
def order_detail(request, transaction_id):
    order = get_object_or_404(Order, transaction_id=transaction_id, user=request.user)
    return render(request, "orders/order_detail.html", {"order": order})
