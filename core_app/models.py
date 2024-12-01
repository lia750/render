from django.db import models

# Service categories for filtering
class Category(models.Model):
    name = models.CharField(max_length=50, choices=[('spa', 'Spa'), ('face', 'Face'), ('eyelash', 'Eyelash & Eyebrow'), ('nails', 'Nails'), ('hair', 'Hair')])

    def __str__(self):
        return self.name

# Service model displayed on the platform
class Service(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in minutes")
    vendor = models.ForeignKey('vendor_app.Vendor', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Home page banner and content
class HomePageContent(models.Model):
    title = models.CharField(max_length=200)
    banner_image = models.ImageField(upload_to='home_banners/')
    description = models.TextField()

    def __str__(self):
        return self.title

