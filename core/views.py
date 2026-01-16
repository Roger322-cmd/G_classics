from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import StaticPage
from catalogue.models import Product, Category

def home(request):
    featured_products = Product.objects.filter(is_featured=True, is_active=True).order_by("-rating")
    high_rated_products = Product.objects.filter(is_active=True).order_by("-rating")
    featured_categories = Category.objects.filter(is_featured=True)[:6]
    
    # Pagination for featured products
    paginator_featured = Paginator(featured_products, 8)
    page_featured = request.GET.get('page_featured')
    
    try:
        featured_products = paginator_featured.page(page_featured)
    except PageNotAnInteger:
        featured_products = paginator_featured.page(1)
    except EmptyPage:
        featured_products = paginator_featured.page(paginator_featured.num_pages)
    
    # Pagination for high rated products
    paginator_rated = Paginator(high_rated_products, 8)
    page_rated = request.GET.get('page_rated')
    
    try:
        high_rated_products = paginator_rated.page(page_rated)
    except PageNotAnInteger:
        high_rated_products = paginator_rated.page(1)
    except EmptyPage:
        high_rated_products = paginator_rated.page(paginator_rated.num_pages)
    
    return render(request, "core/home.html", {
        "featured_products": featured_products,
        "high_rated_products": high_rated_products,
        "featured_categories": featured_categories,
    })


def static_page(request, slug):
    page = get_object_or_404(StaticPage, slug=slug)
    return render(request, "core/static_page.html", {"page": page})
