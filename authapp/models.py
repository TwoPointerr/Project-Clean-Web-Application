from distutils.command.upload import upload
from pyexpat import model
from statistics import mode
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser
from grievance_data.models import *

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(verbose_name='email',max_length=255,unique=True)
    phone = models.CharField(null=True, max_length=255)
    REQUIRED_FIELDS = ['username','phone','first_name','last_name']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email

    def __str__(self) -> str:
        return self.first_name

class CitizenProfile(models.Model):
    citi_user = models.OneToOneField(User,on_delete=models.CASCADE)
    citi_profile_img = models.ImageField(upload_to="profiles_pics",blank=True)

    def __str__(self):
        return self.citi_user.first_name


class MCProfile(models.Model):
    mc_user = models.OneToOneField(User,on_delete=models.CASCADE)
    mc_profile_img = models.ImageField(upload_to="profiles_pics",blank=True)
    mc_employee_id = models.CharField(max_length=250)
    mc_muncipal_co = models.TextField()
    mc_location = models.OneToOneField(Location,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.mc_user.first_name


class Post(models.Model):
    title = models.CharField(null= True,max_length=255)
    post_img = models.ImageField(upload_to="products",blank=True)