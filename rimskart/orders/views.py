from django.shortcuts import render, redirect   
from django.contrib.auth.decorators import login_required
from .models import Order, OrderedItem
from product.models import Product 

@login_required 
def show_cart(request):
    user = request.user
    
    from customers.models import Customer
    customer, created_profile = Customer.objects.get_or_create(user=user)
    
    # Fetch the active cart stage order
    cart_obj = Order.objects.filter(
        owner=customer,
        order_status=Order.CART_STAGE
    ).first()
    
    # Pull items if cart exists
    if cart_obj:
        cart_items = OrderedItem.objects.filter(owner=cart_obj)
    else:
        cart_items = []
        
    # MATCHING VARIABLE NAME: Pass data as 'added_iteams'
    context = {
        'added_iteams': cart_items,
        'cart': cart_obj
    }
    return render(request, 'cart.html', context)

@login_required  
def add_to_cart(request):
    if request.method == 'POST':
        user = request.user
        
        # 1. FIXED: Imported Customer instead of CustomerProfile
        from customers.models import Customer  
        customer, created_profile = Customer.objects.get_or_create(user=user)
        
        quantity = int(request.POST.get('quantity'))
        product_id = request.POST.get('product_id')
        
        product = Product.objects.get(id=product_id)
        
        cart_obj, created = Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        
        ordered_item, created_item = OrderedItem.objects.get_or_create(
            product=product,
            owner=cart_obj,
            defaults={'quantity': quantity}
        )
        
        if not created_item:
            ordered_item.quantity += quantity
            ordered_item.save()
            
        return redirect('show_cart')
