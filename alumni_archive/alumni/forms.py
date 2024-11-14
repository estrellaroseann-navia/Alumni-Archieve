from django import forms
from .models import Alumni

from django.contrib.auth.hashers import make_password

class AlumniRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Alumni
        fields = [
            'first_name', 'middle_initial', 'last_name', 'age', 'birthday', 'address', 
            'year_graduated', 'cluster', 'campus', 'college', 'school_program', 
            'email', 'password', 'terms_accepted'
        ]
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        alumni = super().save(commit=False)
        alumni.password = make_password(self.cleaned_data["password"])
        if commit:
            alumni.save()
        return alumni

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
