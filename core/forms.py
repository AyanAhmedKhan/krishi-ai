from django import forms
from .models import SensorData

class SensorDataForm(forms.ModelForm):
    class Meta:
        model = SensorData
        fields = ['moisture', 'temperature', 'ph'] 