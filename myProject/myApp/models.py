from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError

class AlumniManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class RegisteredAlumni(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = AlumniManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

class YearGraduated(models.IntegerChoices):
    YEAR_2019 = 2019, '2019'
    YEAR_2020 = 2020, '2020'
    YEAR_2021 = 2021, '2021'
    YEAR_2022 = 2022, '2022'
    YEAR_2023 = 2023, '2023'
    YEAR_2024 = 2024, '2024'

class Alumni(models.Model):
    id = models.BigAutoField(primary_key=True)
    lastname = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    middlename = models.CharField(max_length=255)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES) 
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    year_graduated = models.IntegerField(choices=YearGraduated.choices)

    def clean(self):
        if not isinstance(self.year_graduated, int):
            raise ValidationError('Year graduated must be an integer.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
