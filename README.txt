# Krishi AI-Mitra Setup Guide

This guide will help you install dependencies and run the Django project.

---

## 1. Prerequisites
- Python 3.10 or 3.9 (recommended)
- pip (Python package manager)
- (Optional) Virtual environment tool: `venv`

---

## 2. Installation

### a. Clone the repository (if not already done)
```
git clone <your-repo-url>
cd djanogo
```

### b. Create and activate a virtual environment (recommended)
#### On Windows:
```
python -m venv venv
venv\Scripts\activate
```
#### On Mac/Linux:
```
python3 -m venv venv
source venv/bin/activate
```

### c. Install dependencies
```
pip install -r requirements.txt
```

---

## 3. Groq API Key Setup (for AI-powered features)

The app uses Groq's Llama 3 model for fertilizer recommendations.

### a. Get your Groq API key:
- Visit https://console.groq.com/
- Create or log in to your account
- Generate an API key (starts with `gsk_...`)

### b. Set the API key (choose one):
#### Option 1: Environment variable (recommended)
- On Windows (CMD):
  ```
  set GROQ_API_KEY=gsk_your_api_key_here
  ```
- On Windows (PowerShell):
  ```
  $env:GROQ_API_KEY="gsk_your_api_key_here"
  ```
- On Mac/Linux:
  ```
  export GROQ_API_KEY=gsk_your_api_key_here
  ```

#### Option 2: Hardcode in settings (not recommended for production)
- Edit `krishi_ai_mitra/settings.py` or `krishi_ai_mitra/local_settings.py` and set:
  ```python
  GROQ_API_KEY = 'gsk_your_api_key_here'
  ```

---

## 4. Database Setup
- By default, uses SQLite (no setup needed).
- To apply migrations:
```
python manage.py migrate
```

---

## 5. Run the Server
```
python manage.py runserver
```
- Visit http://127.0.0.1:8000/ in your browser.

---

## 6. Admin Panel
- Create a superuser:
```
python manage.py createsuperuser
```
- Access the admin panel at http://127.0.0.1:8000/admin/

---

## 7. Notes
- For AI features, ensure your Groq API key is set.
- For non-AI recommendations, populate the database via the admin panel.
- Static/media files are served automatically in development.

---

## 8. Troubleshooting
- See `API_SETUP.md` for more on Groq API setup and troubleshooting.
- If you see errors about missing dependencies, re-run `pip install -r requirements.txt`.
- For other issues, check Django and dependency documentation. 