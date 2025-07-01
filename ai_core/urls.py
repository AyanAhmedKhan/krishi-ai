from django.urls import path
from . import views

urlpatterns = [
    # Add diagnosis routes here
    path('upload/', views.diagnosis_upload, name='diagnosis_upload'),
    path('result/<int:pk>/', views.diagnosis_result, name='diagnosis_result'),
    path('history/', views.chat_history, name='chat_history'),
] 