import json
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order

@csrf_exempt
def paypal_webhook(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Invalid method")

    payload = request.body.decode("utf-8")
    data = json.loads(payload)

    # Extract transaction id / custom id from PayPal payload
    transaction_id = data.get("resource", {}).get("invoice_id")  # adjust to actual field
    event_type = data.get("event_type")

    if event_type == "CHECKOUT.ORDER.APPROVED" and transaction_id:
        try:
            order = Order.objects.get(transaction_id=transaction_id)
            order.status = "paid"
            order.save()
        except Order.DoesNotExist:
            pass

    return HttpResponse("OK")
