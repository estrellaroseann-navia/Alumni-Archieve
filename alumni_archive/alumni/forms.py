from django import forms
from .models import Alumni

from django.contrib.auth.hashers import make_password

class AlumniRegistrationForm(forms.ModelForm):
    class Meta:
        model = Alumni
        fields = [
            'first_name', 'middle_initial', 'last_name', 'age', 'birthday', 
            'address', 'year_graduated', 'cluster', 'campus', 'college', 
            'school_program', 'email', 'password'
        ]
    
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        
        return cleaned_data

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
