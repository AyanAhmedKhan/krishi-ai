from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sensor/input/', views.sensor_input, name='sensor_input'),
    path('sensor/data/', views.sensor_data_display, name='sensor_data_display'),
    path('admin/analytics/', views.analytics_dashboard, name='analytics_dashboard'),
] 