from ast import arg
from django.db import models
from django.dispatch import receiver
from authapp.models import CitizenProfile, User, MCProfile, Location
from django.db.models.signals import pre_save
import datetime
from PIL import Image
import uuid
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.core.files import File

class Category(models.Model):
    cat_name = models.CharField(max_length=250)
    cat_value = models.IntegerField(default=0)
    def __str__(self):
        return self.cat_name

class Grievance(models.Model):
    gri_img = models.ImageField(upload_to="grievance_pics")
    gri_title = models.CharField(max_length=250)
    gri_desc = models.TextField(null=True)
    gri_category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True, related_name='category')
    gri_upvote = models.PositiveIntegerField(default=0)
    gri_severity = models.IntegerField()
    gri_priority = models.IntegerField()
    gri_uploaded_user = models.ForeignKey(CitizenProfile,on_delete=models.CASCADE, related_name='uploaded_user')
    gri_location = models.OneToOneField(Location,on_delete=models.SET_NULL,null=True)
    gri_timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.gri_title

    def save(self,*args, **kwargs):
        self.gri_img = self.reduce_image_size(self.gri_img) 
        super().save(*args,**kwargs)

    def reduce_image_size(self, profile_pic):
        print(profile_pic)
        img = Image.open(profile_pic)
        thumb_io = BytesIO()
        img.thumbnail((500,668))
        img.save(thumb_io, "jpeg", quality=50)
        new_image = File(thumb_io, name=profile_pic.name)
        return new_image
                 
STATUS_NAME = (
    ("Register","Register"),
    ("Pending","Pending"),
    ("In Progress","In Progress"),
    ("Complete","Complete"),
    ("Rejected","Rejected")
)

class Status(models.Model):
    status_name = models.CharField(max_length=250,choices=STATUS_NAME)
    status_grievance = models.ForeignKey(Grievance,on_delete=models.CASCADE)
    status_active = models.BooleanField(default=False)
    status_timeStamp = models.DateTimeField(auto_now=True)
    status_issuedByMC = models.ForeignKey(MCProfile,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return f"{self.status_grievance} - {self.status_name}"



# Create your models here.
