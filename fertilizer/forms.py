from django import forms
from .models import Crop, SoilType, Region, UserFertilizerRequest

class FertilizerRecommendationForm(forms.ModelForm):
    class Meta:
        model = UserFertilizerRequest
        fields = ['crop', 'soil_type', 'region', 'area_hectares']
        widgets = {
            'crop': forms.Select(attrs={'class': 'form-control'}),
            'soil_type': forms.Select(attrs={'class': 'form-control'}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'area_hectares': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter area in hectares'}),
        }
        labels = {
            'crop': 'Crop Type',
            'soil_type': 'Soil Type',
            'region': 'Region',
            'area_hectares': 'Area (Hectares)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add empty choice for better UX
        self.fields['crop'].empty_label = "Select a crop"
        self.fields['soil_type'].empty_label = "Select soil type"
        self.fields['region'].empty_label = "Select region" 