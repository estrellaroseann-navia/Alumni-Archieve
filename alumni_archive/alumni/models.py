from django.db import models

class Alumni(models.Model):
    first_name = models.CharField(max_length=50)
    middle_initial = models.CharField(max_length=1, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    birthday = models.DateField()
    address = models.CharField(max_length=255)
    year_graduated = models.IntegerField()
    cluster = models.CharField(max_length=50)
    campus = models.CharField(max_length=50, blank=True, null=True)
    college = models.CharField(max_length=50, blank=True, null=True)
    school_program = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  
    terms_accepted = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    

