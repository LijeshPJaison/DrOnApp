from django.db import models

# Create your models here.
class Signup(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    mobile_number = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)

class Booking(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    select_hospital = models.CharField(max_length=200)
    select_department = models.CharField(max_length=200)
    select_doctor = models.CharField(max_length=200)
    date = models.DateField()
    time = models.DateTimeField()