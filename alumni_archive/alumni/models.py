from django.db import models

class Alumni(models.Model):
    first_name = models.CharField(max_length=100)
    middle_initial = models.CharField(max_length=1, blank=True)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    birthday = models.DateField()
    address = models.CharField(max_length=255)
    year_graduated = models.IntegerField()
    cluster = models.CharField(max_length=100)
    campus = models.CharField(max_length=100, blank=True)
    college = models.CharField(max_length=100, blank=True)
    school_program = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

