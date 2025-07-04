from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SensorData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    moisture = models.FloatField()
    temperature = models.FloatField()
    ph = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SensorData by {self.user.username} at {self.created_at.strftime('%Y-%m-%d %H:%M')}"
