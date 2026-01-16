from django.urls import path
from . import webhooks

app_name = "payments"

urlpatterns = [
    path("paypal/webhook/", webhooks.paypal_webhook, name="paypal_webhook"),
]
