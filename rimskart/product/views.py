from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    featured_products = Product.objects.order_by('-priority')[:4]
    latest_products = Product.objects.order_by('-id')[:4]

    context = {
        'featured_products': featured_products,
        'latest_products': latest_products
    }
    return render(request, 'index.html', context)

def products_list(request):
    products = Product.objects.order_by('-priority')
    product_paginator = Paginator(products, 12)
    page = 1
    if request.GET:
        page = request.GET.get('page', 1)
    products = product_paginator.get_page(page)
    context = { 'prod': products }    
    return render(request, 'products_list.html', context)  

def products_detail(request, pk):
    products = Product.objects.get(pk=pk)
    context = {'prod': products}
    return render(request, 'products_detail.html', context)


