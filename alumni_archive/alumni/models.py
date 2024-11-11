from django.db import models

class Alumni(models.Model):
    first_name = models.CharField(max_length=50)
    middle_initial = models.CharField(max_length=1, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    birthday = models.DateField()
    address = models.TextField()
    course = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    cluster = models.CharField(max_length=100)
    year_graduated = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

