from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("transaction_id", "user", "status", "total_amount", "created_at")
    inlines = [OrderItemInline]
    list_filter = ("status",)
