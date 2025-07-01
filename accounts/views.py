from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.views.generic import View
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

class SignupView(View):
    def get(self, request):
        return render(request, 'accounts/signup.html', {'roles': Profile.ROLE_CHOICES})

    def post(self, request):
        form = UserCreationForm(request.POST)
        role = request.POST.get('role', 'farmer')
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, role=role)
            login(request, user)
            messages.success(request, 'Signup successful!')
            return redirect('home')
        return render(request, 'accounts/signup.html', {'form': form, 'roles': Profile.ROLE_CHOICES})

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

class CustomLogoutView(LogoutView):
    next_page = '/'
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
