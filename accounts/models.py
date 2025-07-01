from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    ROLE_CHOICES = [
        ('farmer', 'Farmer'),
        ('admin', 'Admin'),
        ('kiosk', 'Kiosk Operator'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='farmer')

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"
