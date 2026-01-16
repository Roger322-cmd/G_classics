from django.contrib import admin
from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ("price", "subtotal")

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "total_items", "total_price", "updated_at")
    inlines = [CartItemInline]
    readonly_fields = ("updated_at",)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("cart", "variant", "quantity", "price")
    list_filter = ("cart__user",)
    readonly_fields = ("price",)

