from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category

def store(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(is_available=True)

    category = None  # Initialize category outside the if condition

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
        'categories': categories,
        'current_category': category,
    }
    return render(request, 'store/store.html', context)
def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Product.DoesNotExist as e:
        raise e 
    
    context = {
        'single_product': single_product,
    }

    return render(request, 'store/product_detail.html', context)

