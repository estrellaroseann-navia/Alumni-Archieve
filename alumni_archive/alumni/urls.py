from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('homepage/', views.homepage_view, name='homepage'),
    path('adminlogin/', views.adminlogin_view, name='adminlogin'),

    path('forgotpassword/', views.forgotpassword_view, name='forgotpassword'),

    path('confirmlogout/', views.confirmlogout_view, name='confirmlogout'),

    # alumni
    path('alumniprofile/', views.alumniprofile_view, name='alumniprofile'),
    path('alumniprofile/edit-alumniprofile.html/', views.editalumniprofile_view, name='editalumniprofile'),

    # admin
    path('adminhomepage/', views.adminhomepage_view, name='adminhomepage'),
    path('addalumni/', views.addalumni_view, name='addalumni'),
    path('service/', views.services_view, name='service'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('donation/', views.donation_view, name='donation'),

    # survey
    path('survey/', views.survey_view, name='survey'),
    path('survey/page1.html', views.page1_view, name='page1'),
    path('survey/page2.html', views.page2_view, name='page2'),
    path('survey/page3.html', views.page3_view, name='page3'),
    path('survey/page4.html', views.page4_view, name='page4'),
    path('survey/page5.html', views.page5_view, name='page5'),
    path('survey/page6.2.html', views.page6_2_view, name='page6.2'),
    path('survey/page6.html', views.page6_view, name='page6'),
    path('survey/page7.html', views.page7_view, name='page7'),
    path('survey/page8.html', views.page8_view, name='page8'),
    path('survey/page9.html', views.page9_view, name='page9'),
    path('survey/page10.html', views.page10_view, name='page10'),
    path('survey/page11.html', views.page11_view, name='page11'),
    path('survey/page12.html', views.page12_view, name='page12'),
    path('survey/submit.html', views.submit_view, name='submit'),


    

    # Other URLs
    path('get-campuses/', views.get_campuses, name='get_campuses'),
    path('get-programs/', views.get_programs, name='get_programs'),
    path('get-colleges/', views.get_colleges, name='get_colleges'),
    

    




]
