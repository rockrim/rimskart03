from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    products = Product.objects.all()
    product_paginator = Paginator(products, 2)
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    products = product_paginator.get_page(page)
    context = { 'prod': products }
    return render(request,'index.html',context)

def products_list(request):
    products = Product.objects.all()
    context = { 'prod': products }
    return render(request,'products.html', context )  

def products_detail(request):
    return render(request,'products_detail.html')

