# 🌾 Krishi AI-Mitra

<div align="center">

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Groq AI](https://img.shields.io/badge/Groq-AI_Powered-orange?style=for-the-badge&logo=artificial-intelligence)
![Agriculture](https://img.shields.io/badge/Agriculture-Tech-green?style=for-the-badge&logo=leaf&logoColor=white)

**An intelligent agricultural assistant powered by Django and Groq's Llama 3 AI model, providing smart fertilizer recommendations and farming insights.**

[🚀 Quick Start](#-quick-start) • [🔑 API Setup](#-groq-api-configuration) • [🌱 Features](#-features) • [🛠️ Troubleshooting](#-troubleshooting)

</div>

---

## 🌱 Features

<table>
<tr>
<td width="50%">

### 🤖 **AI-Powered Recommendations**
- Smart fertilizer suggestions using Groq's Llama 3
- Personalized farming advice
- Crop-specific recommendations
- Weather-based insights

</td>
<td width="50%">

### 🌾 **Comprehensive Agriculture Tools**
- Soil analysis and recommendations
- Crop management system
- Seasonal planting guides
- Disease and pest identification

</td>
</tr>
<tr>
<td width="50%">

### 📊 **Data Management**
- SQLite database for quick setup
- Django admin panel
- User management system
- Historical data tracking

</td>
<td width="50%">

### 🎯 **User-Friendly Interface**
- Responsive web design
- Multi-language support potential
- Farmer-friendly UI/UX
- Mobile-optimized interface

</td>
</tr>
</table>

---

## 📋 Prerequisites

<details>
<summary>📦 System Requirements</summary>

| Requirement | Version | Purpose |
|-------------|---------|---------|
| **Python** | `3.9` or `3.10` | Core runtime |
| **pip** | Latest | Package management |
| **Git** | Latest | Version control |
| **Virtual Environment** | `venv` (recommended) | Dependency isolation |

### Verify Your Installation
```bash
# Check Python version
python --version  # or python3 --version

# Check pip version
pip --version

# Check Git installation
git --version
```

</details>

---

## 🚀 Quick Start

### 1️⃣ **Clone the Repository**

```bash
# Clone the project
git clone <your-repo-url>
cd djanogo

# Verify project structure
ls -la
```

### 2️⃣ **Set Up Virtual Environment**

<details>
<summary>🪟 Windows Setup</summary>

```bash
# Create virtual environment
python -m venv venv

# Activate environment
venv\Scripts\activate

# Verify activation (you should see (venv) in your prompt)
where python
```

</details>

<details>
<summary>🍎 Mac/Linux Setup</summary>

```bash
# Create virtual environment
python3 -m venv venv

# Activate environment
source venv/bin/activate

# Verify activation (you should see (venv) in your prompt)
which python
```

</details>

### 3️⃣ **Install Dependencies**

```bash
# Install all required packages
pip install -r requirements.txt

# Verify installation
pip list
```

### 4️⃣ **Database Setup**

```bash
# Apply database migrations
python manage.py migrate

# Verify database creation
ls -la  # Look for db.sqlite3 file
```

### 5️⃣ **Launch the Application**

```bash
# Start development server
python manage.py runserver

# Your app will be available at:
# 🌐 http://127.0.0.1:8000/
```

---

## 🔑 Groq API Configuration

### **Get Your API Key**

1. **Visit** [Groq Console](https://console.groq.com/)
2. **Sign up** or log in to your account
3. **Navigate** to API Keys section
4. **Generate** a new API key (format: `gsk_...`)
5. **Copy** your API key securely

### **Configure API Key**

<details>
<summary>🔧 Method 1: Environment Variables (Recommended)</summary>

#### Windows Command Prompt
```cmd
set GROQ_API_KEY=gsk_your_actual_api_key_here
python manage.py runserver
```

#### Windows PowerShell
```powershell
$env:GROQ_API_KEY="gsk_your_actual_api_key_here"
python manage.py runserver
```

#### Mac/Linux Terminal
```bash
export GROQ_API_KEY=gsk_your_actual_api_key_here
python manage.py runserver
```

#### Permanent Setup (Mac/Linux)
```bash
# Add to your shell profile (~/.bashrc, ~/.zshrc, etc.)
echo 'export GROQ_API_KEY=gsk_your_actual_api_key_here' >> ~/.bashrc
source ~/.bashrc
```

</details>

<details>
<summary>⚠️ Method 2: Settings File (Development Only)</summary>

**Note:** Only for development/testing. Never commit API keys to version control.

```python
# In krishi_ai_mitra/settings.py or krishi_ai_mitra/local_settings.py
GROQ_API_KEY = 'gsk_your_actual_api_key_here'
```

Create a `.env` file (recommended):
```env
GROQ_API_KEY=gsk_your_actual_api_key_here
DEBUG=True
SECRET_KEY=your_django_secret_key
```

</details>

---

## 👨‍💼 Admin Panel Setup

### **Create Superuser Account**

```bash
# Create admin user
python manage.py createsuperuser

# Follow the prompts to set:
# - Username
# - Email address  
# - Password (entered twice)
```

### **Access Admin Panel**

1. **Start** the development server: `python manage.py runserver`
2. **Navigate** to: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
3. **Login** with your superuser credentials
4. **Manage** users, data, and application settings

### **Admin Features**
- 👥 User management
- 🌾 Crop data management
- 💊 Fertilizer database
- 📊 Analytics and reports
- ⚙️ System configuration

---

## 🏗️ Project Structure

```
krishi-ai-mitra/
├── 📁 krishi_ai_mitra/          # Main project directory
│   ├── 📄 settings.py           # Django settings
│   ├── 📄 urls.py               # URL routing
│   └── 📄 wsgi.py               # WSGI configuration
├── 📁 apps/                     # Django applications
│   ├── 📁 recommendations/      # AI recommendation engine
│   ├── 📁 crops/               # Crop management
│   └── 📁 users/               # User management
├── 📁 static/                   # Static files (CSS, JS, images)
├── 📁 templates/                # HTML templates
├── 📁 media/                    # User uploaded files
├── 📄 manage.py                 # Django management script
├── 📄 requirements.txt          # Python dependencies
├── 📄 db.sqlite3               # SQLite database (created after migration)
└── 📄 README.md                # This file
```

---

## 🌐 Application URLs

| URL | Description | Purpose |
|-----|-------------|---------|
| [http://127.0.0.1:8000/](http://127.0.0.1:8000/) | **Home Page** | Main application interface |
| [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) | **Admin Panel** | Database and user management |
| [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/) | **API Endpoints** | RESTful API access |
| [http://127.0.0.1:8000/recommendations/](http://127.0.0.1:8000/recommendations/) | **AI Recommendations** | Fertilizer suggestions |

---

## 🛠️ Troubleshooting

<details>
<summary>🐛 Common Issues & Solutions</summary>

### **Installation Problems**

#### Missing Dependencies
```bash
# Reinstall all dependencies
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

#### Python Version Issues
```bash
# Check Python version
python --version

# If wrong version, use specific Python command
python3.9 -m venv venv
# or
python3.10 -m venv venv
```

### **API Key Issues**

#### Groq API Not Working
```bash
# Test API key in Python shell
python manage.py shell

>>> import os
>>> print(os.environ.get('GROQ_API_KEY'))
>>> # Should display your API key
```

#### Environment Variable Not Set
```bash
# Check if environment variable is set
echo $GROQ_API_KEY  # Mac/Linux
echo %GROQ_API_KEY%  # Windows
```

### **Database Problems**

#### Migration Errors
```bash
# Reset migrations (development only)
rm db.sqlite3
python manage.py makemigrations
python manage.py migrate
```

#### Database Locked
```bash
# Stop all Django processes and restart
# On Windows: Ctrl+C then restart
# On Mac/Linux: Ctrl+C then restart
```

### **Server Issues**

#### Port Already in Use
```bash
# Use different port
python manage.py runserver 8001

# Or kill existing process
# Windows: taskkill /f /im python.exe
# Mac/Linux: pkill -f runserver
```

#### Static Files Not Loading
```bash
# Collect static files
python manage.py collectstatic --noinput
```

</details>

---

## 📚 Additional Resources

### **Django Documentation**
- 🔗 [Official Django Docs](https://docs.djangoproject.com/)
- 🔗 [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- 🔗 [Django REST Framework](https://www.django-rest-framework.org/)

### **Groq AI Resources**
- 🔗 [Groq Console](https://console.groq.com/)
- 🔗 [Groq Documentation](https://console.groq.com/docs)
- 🔗 [API Reference](https://console.groq.com/docs/api-reference)

### **Agriculture Tech**
- 🔗 [Precision Agriculture](https://www.fao.org/precision-agriculture/en/)
- 🔗 [Smart Farming Technologies](https://www.un.org/en/desa/smart-farming-technologies)

---

## 🚀 Deployment

<details>
<summary>☁️ Production Deployment Options</summary>

### **Heroku Deployment**
```bash
# Install Heroku CLI
# Create Procfile
echo "web: gunicorn krishi_ai_mitra.wsgi" > Procfile

# Deploy to Heroku
heroku create your-app-name
heroku config:set GROQ_API_KEY=your_api_key
git push heroku main
```

### **Docker Deployment**
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

### **DigitalOcean/AWS**
- Use platforms like DigitalOcean App Platform or AWS Elastic Beanstalk
- Set environment variables in platform settings
- Configure static file serving

</details>

---

## 🤝 Contributing

We welcome contributions to make Krishi AI-Mitra even better!

### **How to Contribute**
1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Make** your changes and test thoroughly
4. **Commit** your changes (`git commit -m 'Add amazing feature'`)
5. **Push** to the branch (`git push origin feature/amazing-feature`)
6. **Open** a Pull Request

### **Development Guidelines**
- Follow Django best practices
- Write tests for new features
- Update documentation as needed
- Ensure mobile responsiveness
- Test AI features with various inputs

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

<div align="center">

**Empowering farmers with AI-driven agricultural intelligence**

Built with ❤️ for the farming community

Special thanks to:
- 🤖 **Groq** for providing powerful AI capabilities
- 🐍 **Django Community** for the robust web framework
- 🌾 **Agricultural Experts** for domain knowledge
- 👨‍💻 **Open Source Contributors** worldwide

---

### 📞 Support

**Need Help?** Check out:
- 📖 `API_SETUP.md` for detailed API configuration
- 🐛 Issues section for bug reports
- 💬 Discussions for community support

⭐ **Star this repository if it helped you!**

</div>
