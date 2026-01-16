from decimal import Decimal
from django.conf import settings
from catalogue.models import ProductVariant

CART_SESSION_ID = "cart"

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart
        self.user = request.user if request.user.is_authenticated else None

    def add(self, variant_id, quantity=1, override_quantity=False):
        variant = ProductVariant.objects.get(id=variant_id)
        variant_id_str = str(variant_id)
        if variant_id_str not in self.cart:
            self.cart[variant_id_str] = {"quantity": 0, "price": str(variant.final_price)}
        if override_quantity:
            self.cart[variant_id_str]["quantity"] = quantity
        else:
            self.cart[variant_id_str]["quantity"] += quantity
        self.save()

    def save(self):
        self.session[CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, variant_id):
        variant_id_str = str(variant_id)
        if variant_id_str in self.cart:
            del self.cart[variant_id_str]
            self.save()

    def __iter__(self):
        variant_ids = self.cart.keys()
        variants = ProductVariant.objects.filter(id__in=variant_ids)
        cart = self.cart.copy()
        for variant in variants:
            item = cart[str(variant.id)]
            item["variant"] = variant
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item["price"]) * item["quantity"] for item in self.cart.values())

    def clear(self):
        self.session[CART_SESSION_ID] = {}
        self.session.modified = True
