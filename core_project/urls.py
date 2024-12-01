from django.contrib import admin
from django.urls import path
from customer_app import views as customer_views
from vendor_app import views as vendor_views
from core_app import views as core_views



urlpatterns = [
    path('admin/', admin.site.urls),
    # Customer URLs
    path('signup/', customer_views.signup, name='customer_signup'),
    path('profile/', customer_views.customer_profile, name='customer_profile'),
    path('dashboard/', customer_views.customer_dashboard, name='customer_dashboard'),
    path('book_service/<int:service_id>/', customer_views.book_service, name='book_service'),
    
    # Vendor URLs
    path('vendor/signup/', vendor_views.vendor_signup, name='vendor_signup'),
    path('vendor/profile/', vendor_views.vendor_profile, name='vendor_profile'),
    path('vendor/dashboard/', vendor_views.vendor_dashboard, name='vendor_dashboard'),
    path('vendor/create_service/', vendor_views.create_service, name='create_service'),
    
    # Core URLs
    path('', core_views.home, name='home'),
    path('services/', core_views.service_list, name='service_list'),
    path('services/<int:service_id>/', core_views.service_detail, name='service_detail'),


    # Login and Logout paths
    path('login/', customer_views.customer_login, name='customer_login'),
    path('logout/', customer_views.customer_logout, name='customer_logout'),
]
