from django.shortcuts import render

def payment_result(request):
    # This can be used after redirect from PayPal or mobile money confirmation
    status = request.GET.get("status", "pending")
    return render(request, "payments/payment_result.html", {"status": status})
