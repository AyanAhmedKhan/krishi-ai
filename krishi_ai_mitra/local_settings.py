# Local settings for Krishi AI-Mitra
# Copy this file to local_settings.py and add your API keys

import os

# Groq API Configuration
GROQ_API_KEY = os.getenv('GROQ_API_KEY', 'your_groq_api_key_here')

# Django Secret Key (generate a new one for production)
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-your-secret-key-here')

# Debug settings
DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static and Media files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media' 