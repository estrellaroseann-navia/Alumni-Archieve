from os import renames
from tkinter.messagebox import RETRY
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

# def homepage_view(request):
#     alumni_id = request.session.get('alumni_id')
#     if not alumni_id:
#         # Redirect to login or handle the case when alumni_id is missing
#         return redirect('login')  # or an appropriate URL name

def homepage_view(request):
    return render(request, 'homepage.html' )

def forgotpassword_view(request):
    return render(request, 'forgotpassword.html' ) 

def about_view(request):
    return render(request, 'about.html' )

def contact_view(request):
    return render(request, 'contact.html' )

def donation_view(request):
    return render(request, 'donation.html' )

# admin pages
def adminlogin_view(request):
    return render(request, 'adminlogin.html' )

def adminhomepage_view (request):
    return render(request, 'adminhomepage.html' )

def addalumni_view(request):
    return render(request, 'addalumni.html' )

def services_view(request):
    return render(request, 'service.html' )

# alumni pages
def confirmlogout_view(request):
    return render(request, 'confirmlogout.html' )

def alumniprofile_view(request):
    return render(request, 'alumniprofile.html' )

def editalumniprofile_view(request):
    return render(request, 'edit-alumniprofile.html' )

# survey
def survey_view(request):
    return render(request, 'survey.html' )

def page1_view(request):
    return render(request, 'page1.html' )

def page2_view(request):
    return render(request, 'page2.html' )

def page3_view(request):
    return render(request, 'page3.html' )

def page4_view(request):
    return render(request, 'page4.html' )

def page5_view(request):
    return render(request, 'page5.html' )

def page6_2_view(request):
    return render(request, 'page6.2.html' )

def page6_view(request):
    return render(request, 'page6.html' )

def page7_view(request):
    return render(request, 'page7.html' )

def page8_view(request):
    return render(request, 'page8.html' )

def page9_view(request):
    return render(request, 'page9.html' )

def page10_view(request):
    return render(request, 'page10.html' )

def page11_view(request):
    return render(request, 'page11.html' )

def page12_view(request):
    return render(request, 'page12.html' )

