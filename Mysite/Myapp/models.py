from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    phone= models.CharField(max_length=10)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    cus_img = models.ImageField(upload_to='img')
