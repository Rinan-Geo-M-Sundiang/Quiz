from django.db import models
from account.models import MyUser  # Import the custom user model

class BloodDonationRequest(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    request_type = models.CharField(choices=[('donating', 'Donating'), ('looking', 'Looking')], max_length=10)
    blood_type = models.CharField(max_length=3)
    region = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
