from django.contrib import admin
from .models import Crop, SoilType, Region, Fertilizer, FertilizerRecommendation, UserFertilizerRequest

@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ['name', 'hindi_name', 'description']
    search_fields = ['name', 'hindi_name']
    list_filter = ['name']

@admin.register(SoilType)
class SoilTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'hindi_name', 'description']
    search_fields = ['name', 'hindi_name']
    list_filter = ['name']

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name', 'hindi_name', 'state']
    search_fields = ['name', 'hindi_name', 'state']
    list_filter = ['state']

@admin.register(Fertilizer)
class FertilizerAdmin(admin.ModelAdmin):
    list_display = ['name', 'npk_ratio', 'description', 'application_rate']
    search_fields = ['name', 'description']
    list_filter = ['npk_ratio']

@admin.register(FertilizerRecommendation)
class FertilizerRecommendationAdmin(admin.ModelAdmin):
    list_display = ['crop', 'soil_type', 'region', 'primary_fertilizer', 'secondary_fertilizer']
    list_filter = ['crop', 'soil_type', 'region']
    search_fields = ['crop__name', 'soil_type__name', 'region__name']

@admin.register(UserFertilizerRequest)
class UserFertilizerRequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'crop', 'soil_type', 'region', 'area_hectares', 'created_at']
    list_filter = ['crop', 'soil_type', 'region', 'created_at']
    search_fields = ['user__username', 'crop__name', 'soil_type__name', 'region__name']
    readonly_fields = ['created_at']
