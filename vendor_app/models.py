from django.db import models
from django.contrib.auth.models import User

# Vendor model extending the built-in User model
class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=200)
    business_description = models.TextField()
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.business_name

# Vendor service model
class Service(models.Model):
    vendor = models.ForeignKey(Vendor, related_name='services', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in minutes")
    category = models.CharField(max_length=50, choices=[('spa', 'Spa'), ('face', 'Face'), ('eyelash', 'Eyelash & Eyebrow'), ('nails', 'Nails'), ('hair', 'Hair')])

    def __str__(self):
        return self.name
