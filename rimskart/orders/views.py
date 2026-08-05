from django.shortcuts import render, redirect   
from .models import Order, OrderedItem
from product.models import Product
from customers.models import Customer 
from django.contrib.auth.decorators import login_required #decorator needed to check if user is logged in or not, if not then redirect to login page
from django.contrib import messages

@login_required 
def show_cart(request):
    #evaluating the userprofile
    user = request.user # checking sectionID from the coockies  
    customer, created_profile = Customer.objects.get_or_create(user=user) # creating userprofile
    cart_obj = Order.objects.filter(owner=customer,order_status=Order.CART_STAGE).first() 


    if cart_obj:
        cart_items = OrderedItem.objects.filter(owner=cart_obj)
        cart_subtotal = sum(item.product.price * item.quantity for item in cart_items)
    else:
        cart_items = []
        cart_subtotal = 0
        
    context = {
        'cart': cart_obj,
        'added_items': cart_items, 
        'cart_subtotal': cart_subtotal,                    
        'grand_total': cart_subtotal + 18 if cart_subtotal > 0 else 0 
    }
    return render(request, 'cart.html', context)


@login_required  
def add_to_cart(request):
    if request.method == 'POST':
        user = request.user
        customer, created_profile = Customer.objects.get_or_create(user=user)
        
        quantity = int(request.POST.get('quantity'))
        product_id = request.POST.get('product_id')
        
        product = Product.objects.get(id=product_id)
        
        cart_obj, new_created = Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        
        ordered_item, new_created_item = OrderedItem.objects.get_or_create(
            product=product,
            owner=cart_obj,
            defaults={'quantity': quantity}
        )
        
        if not new_created_item:
            ordered_item.quantity += quantity
            ordered_item.save() 
            
        return redirect('show_cart') 

@login_required
def remove_from_cart(request, pk):  
    try:
        item = OrderedItem.objects.get(id=pk, owner__owner__user=request.user)
        item.delete()  
    except OrderedItem.DoesNotExist:
        pass
    return redirect('show_cart')


@login_required  
def checkout_cart(request):
    if request.method == 'POST':

        try:
            user = request.user 
            customer =user.customer_profile        
            total = float(request.POST.get('total'))
            order_obj = Order.objects.get(
                owner=customer,
                order_status=Order.CART_STAGE
            )

            if order_obj:
                order_obj.order_status=Order.ORDER_CONFIRMED
                order_obj.save()
                status_message= "your order has been placed successfully"
                messages.success(request, status_message)

            else:
                status_message = "no iteam in cart" 
                messages.error(request, status_message)

        except Exception as e:
            status_message = "An error occurred while processing your order."
            messages.error(request, status_message)
            print(f"Error during checkout: {e}")

    return redirect ("show_cart")                
















      
 