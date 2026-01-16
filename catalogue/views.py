from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, Category
from .filters import filter_products

def product_list(request):
    products = Product.objects.filter(is_active=True)
    products = filter_products(products, request.GET)
    categories = Category.objects.filter(parent__isnull=True)
    
    # Pagination
    paginator = Paginator(products, 50)
    page = request.GET.get('page')
    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    
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


def search(request):
    query = request.GET.get("q", "").strip()
    products = Product.objects.filter(is_active=True)
    
    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        )
    
    categories = Category.objects.filter(parent__isnull=True)
    
    # Pagination
    paginator = Paginator(products, 50)
    page = request.GET.get('page')
    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    
    return render(request, "catalogue/search_results.html", {
        "products": products,
        "categories": categories,
        "query": query,
    })


def search_autocomplete(request):
    query = request.GET.get("q", "").strip()
    
    if len(query) < 2:
        return JsonResponse({"results": []})
    
    products = Product.objects.filter(
        is_active=True,
        name__icontains=query
    ).values("name", "slug")[:8]
    
    results = [
        {
            "name": product["name"],
            "slug": product["slug"],
        }
        for product in products
    ]
    
    return JsonResponse({"results": results})
