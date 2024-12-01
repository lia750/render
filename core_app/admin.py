from django.contrib import admin
from .models import Service, HomePageContent, Category
from vendor_app.models import Vendor, Service as VendorService
from customer_app.models import Customer, Booking

# Register models to be accessible via Django admin
admin.site.register(Vendor)
admin.site.register(VendorService)
admin.site.register(Customer)
admin.site.register(Booking)
admin.site.register(Service)
admin.site.register(HomePageContent)
admin.site.register(Category)
