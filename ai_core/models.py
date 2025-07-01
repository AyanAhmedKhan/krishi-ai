from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Diagnosis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='diagnosis/')
    result = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    gemini_response = models.TextField(blank=True)
    gemini_response_en = models.TextField(blank=True)
    gemini_response_hi = models.TextField(blank=True)
    audio_en = models.FileField(upload_to='audio/', blank=True, null=True)
    audio_hi = models.FileField(upload_to='audio/', blank=True, null=True)

    def __str__(self):
        return f"Diagnosis by {self.user.username} at {self.created_at.strftime('%Y-%m-%d %H:%M')}"

class DiagnosisHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE, related_name='history')
    chat_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"History for {self.diagnosis} at {self.created_at.strftime('%Y-%m-%d %H:%M')}"
