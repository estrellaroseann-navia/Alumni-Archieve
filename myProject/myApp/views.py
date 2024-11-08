from multiprocessing import context
from operator import imod
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import Alumni
from django.contrib.auth.forms import UserCreationForm

from .models import *
from .forms import RegistrationForm

from .decorators import allowed_users, unauthenticated_user


def landingpage(request):
    return render(request, 'landingpage.html')


# for sign up and login and logout

def usersignup(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        form = RegistrationForm()
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save() 
                messages.success(request, f'Account created for {user.first_name}')
                return redirect('userlogin')  

        context = {'form': form}
        return render(request, 'signup.html', context)

@unauthenticated_user
def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.info(request, 'Username or Password is incorrect!')

    context = {}
    return render (request, 'login.html', context)

def userconfirmlogout(request):
    return render (request, 'confirmlogout.html')

def userlogout(request):
    logout(request)
    return redirect('userlogin')


@login_required(login_url='userlogin')
@allowed_users(allowed_roles=['admin'])
def adminhomepage(request):
    return render(request, 'adminhomepage.html')

@login_required(login_url='userlogin')
@allowed_users(allowed_roles=['alumni'])
def homepage(request):
    return render(request, 'homepage.html')

# end of sign up and log in

@login_required(login_url='userlogin')
def about(request):
    return render(request, 'about.html')

@login_required(login_url='userlogin')
def contact(request):
    return render(request, 'contact.html')

@login_required(login_url='userlogin')
def survey(request):
    return render(request, 'survey.html')

@login_required(login_url='userlogin')
def forgotpassword(request):
    return render(request, 'forgotpassword.html')

@login_required(login_url='userlogin')
def donation(request):
    return render (request, 'donation.html')

def alumni(request):
    alum=Alumni.objects.all()
    return render(request, 'alumni.html', {'alum': alum})