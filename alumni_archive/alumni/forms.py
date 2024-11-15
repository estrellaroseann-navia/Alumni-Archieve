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


class AlumniRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}))

    cluster = forms.ChoiceField(choices=CLUSTER_CHOICES, widget=forms.Select(attrs={'id': 'id_cluster', 'placeholder': 'Select your cluster'}))
    campus = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={'id': 'id_campus', 'placeholder': 'Select Campus'}))
    college = forms.ChoiceField(choices=COLLEGE_CHOICES,required=True, widget=forms.Select(attrs={'id': 'id_college', 'placeholder': 'Select College'}))
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
        self.fields["campus"].choices = CAMPUS_CHOICES.get(self.data.get('cluster'), [])
        self.fields["school_program"].choices = PROGRAM_CHOICES.get(self.data.get('college'), [])

        
    
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)