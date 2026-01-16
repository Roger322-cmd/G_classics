from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from .filters import filter_products

def product_list(request):
    products = Product.objects.filter(is_active=True)
    products = filter_products(products, request.GET)
    categories = Category.objects.filter(parent__isnull=True)
    return render(request, "catalogue/product_list.html", {
        "products": products,
        "categories": categories,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    variants = product.variants.all()
    return render(request, "catalogue/product_detail.html", {
        "product": product,
        "variants": variants,
    })
