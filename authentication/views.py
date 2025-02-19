from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, LoginForm
from .models import CustomUser

# Register View
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect("dashboard")  # Ensure "dashboard" exists in urls.py
    else:
        form = CustomUserCreationForm()
    
    return render(request, "authentication/register.html", {"form": form})

# Login View
def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profile")  # Ensure "profile" exists in urls.py
    else:
        form = LoginForm()

    return render(request, "authentication/login.html", {"form": form})

# Logout View
@login_required
def logout_view(request):
    logout(request)
    return redirect("login")

# Profile View
@login_required  # Ensure only logged-in users access profile
def profile_view(request):
    return render(request, "authentication/profile.html")

from django.shortcuts import render

def register_view(request):
    return render(request, "authentication/register.html")  # Ensure correct path

def login_view(request):
    return render(request, "authentication/login.html")

def logout_view(request):
    return render(request, "authentication/logout.html")

