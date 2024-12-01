from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import VendorProfileForm, ServiceForm
from .models import Vendor, Service
from django.contrib.auth.decorators import login_required

# Vendor Sign-Up
def vendor_signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Create the vendor profile
            Vendor.objects.create(user=user)
            return redirect('vendor_dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'vendor_app/vendor_signup.html', {'form': form})

# Vendor Profile Update
@login_required
def vendor_profile(request):
    vendor = Vendor.objects.get(user=request.user)
    if request.method == "POST":
        form = VendorProfileForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
            return redirect('vendor_dashboard')
    else:
        form = VendorProfileForm(instance=vendor)
    return render(request, 'vendor_app/vendor_profile.html', {'form': form})

# Vendor Dashboard (view services and bookings)
@login_required
def vendor_dashboard(request):
    vendor = Vendor.objects.get(user=request.user)
    services = Service.objects.filter(vendor=vendor)
    return render(request, 'vendor_app/vendor_dashboard.html', {'services': services})

# Create/Update Service
@login_required
def create_service(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.vendor = Vendor.objects.get(user=request.user)
            service.save()
            return redirect('vendor_dashboard')
    else:
        form = ServiceForm()
    return render(request, 'vendor_app/create_service.html', {'form': form})



"""
1. vendor_app/vendor_signup.html
2. vendor_app/vendor_profile.html
3. vendor_dashboard.html
4. vendor_app/create_service.html

"""