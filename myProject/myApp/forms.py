from dataclasses import field
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import RegisteredAlumni


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 


class RegistrationForm(forms.ModelForm):  
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    school_id = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'ID Number'}))
    corporate_email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Corporate Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}))

    class Meta:
        model = RegisteredAlumni
        fields = ['first_name', 'last_name', 'school_id', 'corporate_email']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError("Passwords don't match.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
