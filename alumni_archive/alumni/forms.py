from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Row, Column, Submit
from .models import Alumni

from django.contrib.auth.hashers import make_password

class AlumniRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Alumni
        fields = [
            'first_name', 'middle_initial', 'last_name', 'age', 'birthday', 
            'address', 'course', 'college', 'cluster', 'year_graduated', 
            'email', 'password'
        ]

    def __init__(self, *args, **kwargs):
        super(AlumniRegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Personal Information',
                Row(
                    Column('first_name', css_class='form-group col-md-6'),
                    Column('middle_initial', css_class='form-group col-md-2'),
                    Column('last_name', css_class='form-group col-md-4')
                ),
            ),
            Fieldset(
                'Detailed Information',
                Row(
                    Column('age', css_class='form-group col-md-6'),
                    Column('birthday', css_class='form-group col-md-6')
                ),
                'address',
            ),
            Fieldset(
                'Academic Information',
                'course',
                'college',
                'cluster',
                'year_graduated',
            ),
            Fieldset(
                'Account Information',
                'email',
                'password',
            ),
            Submit('submit', 'Register Account', css_class='btn btn-primary btn-block')
        )
        self.helper.form_method = 'POST'

    def save(self, commit=True):
        alumni = super(AlumniRegistrationForm, self).save(commit=False)
        alumni.password = make_password(self.cleaned_data['password'])  # Hash the password
        if commit:
            alumni.save()
        return alumni

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
