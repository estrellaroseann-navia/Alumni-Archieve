from os import renames
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import AlumniRegistrationForm, LoginForm
from .models import Alumni

def landingpage(request):
    return render(request, 'landingpage.html')

def register_view(request):
    if request.method == 'POST':
        form = AlumniRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect('login')  # Redirect to the login page
    else:
        form = AlumniRegistrationForm()  
    
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                alumni = Alumni.objects.get(email=email)
                if alumni.password == password:
                    request.session['alumni_id'] = alumni.id
                    messages.success(request, f"Welcome {alumni.first_name}!")
                    return redirect('homepage')
                else:
                    messages.error(request, "Invalid email or password")
            except Alumni.DoesNotExist:
                messages.error(request, "Invalid email or password")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def homepage_view(request):
    alumni_id = request.session.get('alumni_id')
    if not alumni_id:
        # Redirect to login or handle the case when alumni_id is missing
        return redirect('login')  # or an appropriate URL name

def forgotpassword_view(request):
    return render(request, 'forgotpassword.html') 

def adminlogin_view(request):
    return render(request, 'adminlogin.html' )