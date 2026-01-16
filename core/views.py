from django.shortcuts import render, get_object_or_404
from .models import StaticPage
from catalogue.models import Product, Category

def home(request):
    featured_products = Product.objects.filter(is_featured=True).order_by("-rating")[:8]
    high_rated_products = Product.objects.order_by("-rating")[:8]
    featured_categories = Category.objects.filter(is_featured=True)[:6]
    return render(request, "core/home.html", {
        "featured_products": featured_products,
        "high_rated_products": high_rated_products,
        "featured_categories": featured_categories,
    })


def static_page(request, slug):
    page = get_object_or_404(StaticPage, slug=slug)
    return render(request, "core/static_page.html", {"page": page})
