from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import CustomerProfileForm
from .models import Customer, Booking
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Customer Sign-Up
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Create the customer profile
            Customer.objects.create(user=user)
            return redirect('customer_dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'customer_app/signup.html', {'form': form})


# Custom login view (if needed for custom template)
def customer_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('customer_dashboard')
        else:
            messages.error(request, "Invalid credentials")
    else:
        form = AuthenticationForm()
    
    return render(request, 'customer_app/login.html', {'form': form})


# Logout view
def customer_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('customer_login')









# Customer Profile
@login_required
def customer_profile(request):
    customer = Customer.objects.get(user=request.user)
    if request.method == "POST":
        form = CustomerProfileForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_dashboard')
    else:
        form = CustomerProfileForm(instance=customer)
    return render(request, 'customer_app/customer_profile.html', {'form': form})

# Customer Dashboard
@login_required
def customer_dashboard(request):
    customer = Customer.objects.get(user=request.user)
    bookings = Booking.objects.filter(customer=customer)
    return render(request, 'customer_app/customer_dashboard.html', {'bookings': bookings})

# Booking a service (via the core app)
@login_required
def book_service(request, service_id):
    # Here we assume service_id is passed and exists
    # This can be modified to handle booking confirmation
    return HttpResponse(f"Service {service_id} booked successfully!")









"""
Template pages:
1. customer_app/signup.html
2. customer_app/customer_profile.html
3. customer_app/customer_dashboard.html
4. customer_app/login.html
5. 
"""