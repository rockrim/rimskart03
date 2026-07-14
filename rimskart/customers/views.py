from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Customer
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout as log_out

# Create your views here.
def show_account(request):
    if request.method == 'POST' and 'register' in request.POST:
        try:
            # Handle registration logic here
            username = request.POST.get('username')
            password = request.POST.get('password')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            email = request.POST.get('email')

            # 1. Correctly create the built-in Django user
            user = User.objects.create_user(
                username=username,
                password=password, 
                email=email
            )
            
            # 2. FIX: Use your Customer model instead of User.objects.create_user
            customer = Customer.objects.create(
                user=user,
                address=address, 
                phone=phone
            )
            
            messages.success(request, "Registration successful!")
            return redirect('show_account') # Redirect prevents resubmitting form on refresh
            
        except Exception as e:
            error_message = "An error occurred during registration: " + str(e)
            messages.error(request, error_message)
    if request.method == 'POST' and 'login' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'account.html')

def signout(request):
    log_out (request)
    return redirect ('account')

