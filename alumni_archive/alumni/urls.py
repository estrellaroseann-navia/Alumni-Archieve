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
]
