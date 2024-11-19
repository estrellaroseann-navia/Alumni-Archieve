from django import forms
from .models import Alumni
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError

from django.contrib.auth.hashers import make_password

CLUSTER_CHOICES = [
        ('', 'Select Cluster'),
        ('main', 'Main Campus'),
        ('cluster1', 'Cluster 1'),
        ('cluster2', 'Cluster 2'),
        ('cluster3', 'Cluster 3'),
        ('cluster4', 'Cluster 4'),
        ('cuyo', 'PCAT Cuyo'),
    ]


class AlumniRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}))

    cluster = forms.ChoiceField(choices=CLUSTER_CHOICES, widget=forms.Select(attrs={'id': 'id_cluster', 'placeholder': 'Select your cluster'}))
    campus = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={'id': 'id_campus', 'placeholder': 'Select Campus'}))
    college = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={'id': 'id_college', 'placeholder': 'Select College'}))
    school_program = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={'id': 'id_school_program', 'placeholder': 'Select Program'}))

    #validate email if exist then throw error
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Alumni.objects.filter(email=email).exists():
            raise ValidationError("This email address is already registered.")
        return email

    #validate if term not accepted
    def clean_terms_accepted(self):
        terms_accepted = self.cleaned_data.get('terms_accepted')
        if not terms_accepted:
            raise ValidationError("You must accept the terms and conditions to register.")
        return terms_accepted


    class Meta:
        model = Alumni
        fields = "__all__"
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'middle_initial': forms.TextInput(attrs={'placeholder': 'M'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age'}),
            'birthday': DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address'}),
            'year_graduated': forms.NumberInput(attrs={'placeholder': 'Year Graduated'}),
            'cluster': forms.TextInput(attrs={'placeholder': 'Cluster'}),
            'campus': forms.TextInput(attrs={'placeholder': 'Campus (optional)'}),
            'college': forms.TextInput(attrs={'placeholder': 'College (optional)'}),
            'school_program': forms.TextInput(attrs={'placeholder': 'School Program (optional)'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["campus"].choices = ""
        self.fields["school_program"].choices = ""

        
    
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)