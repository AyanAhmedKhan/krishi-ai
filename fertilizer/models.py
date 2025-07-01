from django.db import models
from django.contrib.auth.models import User

class Crop(models.Model):
    name = models.CharField(max_length=100)
    hindi_name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class SoilType(models.Model):
    name = models.CharField(max_length=100)
    hindi_name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=100)
    hindi_name = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.name

class Fertilizer(models.Model):
    name = models.CharField(max_length=100)
    hindi_name = models.CharField(max_length=100, blank=True)
    npk_ratio = models.CharField(max_length=20, blank=True)  # e.g., "10-26-26"
    description = models.TextField(blank=True)
    application_rate = models.CharField(max_length=100, blank=True)  # e.g., "250-300 kg/ha"
    
    def __str__(self):
        return self.name

class FertilizerRecommendation(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    soil_type = models.ForeignKey(SoilType, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    primary_fertilizer = models.ForeignKey(Fertilizer, on_delete=models.CASCADE, related_name='primary_recommendations')
    secondary_fertilizer = models.ForeignKey(Fertilizer, on_delete=models.CASCADE, related_name='secondary_recommendations', null=True, blank=True)
    organic_fertilizer = models.CharField(max_length=200, blank=True)
    application_timing = models.TextField(blank=True)
    special_notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.crop.name} - {self.region.name} - {self.primary_fertilizer.name}"

class UserFertilizerRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    soil_type = models.ForeignKey(SoilType, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    area_hectares = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    recommendation = models.ForeignKey(FertilizerRecommendation, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.crop.name} - {self.created_at.date()}"
