from django.urls import path
from . import views

urlpatterns = [
    path('', views.fertilizer_home, name='fertilizer'),
    path('recommendation/', views.fertilizer_recommendation, name='fertilizer_recommendation'),
    path('history/', views.fertilizer_history, name='fertilizer_history'),
    # Add fertilizer recommendation routes here
] 