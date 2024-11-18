from os import renames
from tkinter.messagebox import RETRY
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import AlumniRegistrationForm, LoginForm
from .models import Alumni

from django.http import JsonResponse


CAMPUS_CHOICES = {
    '':[''],
    'main': [
        ('maincampus', 'Puerto Princesa City')
    ],
    'cluster1': [
        ('cluster1campus1', 'ROXAS'),
        ('cluster1campus2', 'ARACELI'),
        ('cluster1campus3', 'DUMARAN'),
        ('cluster1campus4', 'SAN VICENTE')
    ],
    'cluster2': [
        ('cluster2campus1', 'TAYTAY'),
        ('cluster2campus2', 'EL NIDO'),
        ('cluster2campus3', 'NILAPACAN'),
        ('cluster2campus4', 'CORON')
    ],
    'cluster3': [
        ('cluster3campus1', 'NARRA'),
        ('cluster3campus2', 'QUEZON'),
        ('cluster3campus3', 'RIZAL')
    ],
    'cluster4': [
        ('cluster4campus1', 'ESPANOLA'),
        ('cluster4campus2', 'BROOKES POINT'),
        ('cluster4campus3', 'ESPANOLA'),
        ('cluster4campus4', 'BATARAZA')
    ],
    'cuyo': [
        ('cuyocampus1', 'CUYO')
    ]
}

COLLEGE_CHOICES = [
    ('', 'Select College'),
    ('cs', 'College of Sciences'),
    ('ceat', 'College of Engineering Architecture and Technology'),
    ('cah', 'College of Arts and Humanities'),
    ('cba', 'College of Business and Accountancy'),
    ('ccje', 'College of Criminal Justice Education'),
    ('cte', 'College of Teacher Education'),
    ('chtm', 'College of Nursing and Health Sciences'),
    ('ceat', 'College of Hospitality Management and Tourism'),
    ('graduate-school', 'College of PSU-Graduate School')
]

PROGRAM_CHOICES = {
    'cs': [
        ('bio', 'Bachelor of Science in Biology'),
        ('marbio', 'Bachelor of Science in Marine Biology'),
        ('comsci', 'Bachelor of Science in Computer Science'),
        ('envisci', 'Bachelor of Science in Environmental Science'),
        ('it', 'Bachelor of Science in Information Technology')
    ],
    'ceat': [
        ('archi', 'Bachelor of Science in Architecture'),
        ('civil', 'Bachelor of Science in Civil Engineering'),
        ('elect', 'Bachelor of Science in Electrical Engineering'),
        ('peteng', 'Bachelor of Science in Petroleum Engineering')
    ],
    'cah': [
        ('com', 'Bachelor of Arts in Communication'),
        ('polsci', 'Bachelor of Arts in Political Science'),
        ('solwork', 'Bachelor of Arts in Social Work'),
        ('psych', 'Bachelor of Arts in Psychology')
    ],
    'cba': [
        ('accountancy', 'Bachelor of Science in Accountancy'),
        ('manaccount', 'Bachelor of Science in Management Accounting'),
        ('bus-add', 'Bachelor of Science in Business Administration'),
        ('entrep', 'Bachelor of Science in Entrepreneurship'),
        ('fm', 'Bachelor of Science in Financial Management')
    ],
    'ccje': [
        ('crim', 'Bachelor of Science in Criminology'),
        ('program10', 'Program 10')  # Placeholder program name
    ],
    'cte': [
        ('bee', 'Bachelor of Elementary Education'),
        ('bse', 'Bachelor of Secondary Education'),
        ('bpe', 'Bachelor of Physical Education')
    ],
    'cnhs': [
        ('bsn', 'Bachelor of Science in Nursing'),
        ('bsm', 'Bachelor of Science in Midwifery'),
        ('diploma', 'Diploma in Midwifery')
    ],
    'chtm': [
        ('hm', 'Bachelor of Science in Hospitality Management'),
        ('btm', 'Bachelor of Science in Tourism Management'),
        ('diploma', 'Diploma in Midwifery')
    ],
    'graduate-school': [
        ('de', 'Doctor of Education'),
        ('mba', 'Master of Business Administration'),
        ('mst', 'Master of Science in Technopreneurship'),
        ('mat', 'Master of Arts in Teaching'),
        ('msem', 'Master of Science in Environmental Management'),
        ('mpa', 'Master in Public Administration'),
        ('msn', 'Master of Science in Nursing')
    ]
}


def get_campuses(request):
    cluster = request.GET.get('cluster')
    campuses = CAMPUS_CHOICES.get(cluster, [])
    return JsonResponse({'campuses': campuses})

def get_colleges(request):
    colleges = COLLEGE_CHOICES
    return JsonResponse({'colleges': colleges})


def get_programs(request):
    college = request.GET.get('college')
    programs = PROGRAM_CHOICES.get(college, [])
    return JsonResponse({'programs': programs})


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

def submit_view(request):
    return render(request, 'submit.html' )

