from django.shortcuts import render, get_object_or_404, redirect
from .models import Service, HomePageContent, Category
from django.contrib.auth.decorators import login_required
from customer_app.models import Booking
from vendor_app.models import Vendor

# Home Page View
def home(request):
    home_content = HomePageContent.objects.all()
    return render(request, 'core_app/home.html', {'home_content': home_content})

# Service List (Display all services)
def service_list(request):
    services = Service.objects.all()
    return render(request, 'core_app/service_list.html', {'services': services})

# Service Details (Detailed view of each service)
def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'core_app/service_detail.html', {'service': service})

# Booking a Service
@login_required
def book_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    vendor = service.vendor
    customer = request.user.customer
    booking = Booking.objects.create(customer=customer, service=service, vendor=vendor, status="pending")
    return redirect('customer_dashboard')



"""
1. core_app/home.html
2. core_app/service_list.html
3. core_app/service_detail.html
"""