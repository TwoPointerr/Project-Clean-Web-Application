from django.db import models
from authapp.models import CitizenProfile, User, MCProfile, Location
import datetime


class Category(models.Model):
    cat_name = models.CharField(max_length=250)
    cat_value = models.IntegerField(default=0)
    def __str__(self):
        return self.cat_name

class Grievance(models.Model):
    gri_img = models.ImageField(upload_to="grievance_pics")
    gri_title = models.CharField(max_length=250)
    gri_desc = models.TextField(null=True)
    gri_category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    gri_upvote = models.PositiveIntegerField(default=0)
    gri_severity = models.IntegerField()
    gri_priority = models.IntegerField()
    gri_uploaded_user = models.ForeignKey(CitizenProfile,on_delete=models.CASCADE)
    gri_location = models.OneToOneField(Location,on_delete=models.SET_NULL,null=True)
    gri_timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.gri_title

class Status(models.Model):
    status_name = models.CharField(max_length=250)
    status_grievance = models.ForeignKey(Grievance,on_delete=models.CASCADE)
    status_active = models.BooleanField(default=False)
    status_timeStamp = models.DateTimeField(auto_now=True)
    status_issuedByMC = models.ForeignKey(MCProfile,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.status_name



# Create your models here.
