from .models import Product

def filter_products(queryset, params):
    category_slug = params.get("category")
    min_price = params.get("min_price")
    max_price = params.get("max_price")
    min_rating = params.get("min_rating")

    if category_slug:
        queryset = queryset.filter(category__slug=category_slug)
    if min_price:
        queryset = queryset.filter(base_price__gte=min_price)
    if max_price:
        queryset = queryset.filter(base_price__lte=max_price)
    if min_rating:
        queryset = queryset.filter(rating__gte=min_rating)

    return queryset
