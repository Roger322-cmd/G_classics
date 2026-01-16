from django.conf import settings

def create_paypal_order(order):
    """
    Call PayPal API to create an order and return approval URL / id.
    This is a placeholder; plug in PayPal SDK or REST calls here.
    """
    # pseudo-code
    return {
        "id": order.transaction_id,
        "approval_url": "https://www.sandbox.paypal.com/checkoutnow?token=EXAMPLE",
    }
