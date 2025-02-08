from django.shortcuts import render, redirect ,get_object_or_404

# Create your views here.
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'cart/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'cart/product_detail.html', {'product': product})