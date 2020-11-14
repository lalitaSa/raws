from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    phone= models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    dob = models.DateField(max_length=8)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    school = models.CharField(max_length=50)
    cus_img = models.ImageField(upload_to='img')
