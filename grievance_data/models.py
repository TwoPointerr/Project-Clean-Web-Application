from django.db import models
from authapp.models import CitizenProfile, User, MCProfile


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

    def __str__(self):
        return self.gri_title

class Location(models.Model):
    loc_long = models.FloatField()
    loc_lat = models.FloatField()
    loc_display_name = models.TextField()
    loc_suburb = models.CharField(max_length=250)
    loc_town = models.CharField(max_length=250)
    loc_city = models.CharField(max_length=250)
    loc_municipality = models.TextField()
    loc_state_distric = models.CharField(max_length=250)
    loc_state = models.CharField(max_length=250)
    loc_postcode = models.PositiveIntegerField()

    def __str__(self):
        return self.loc_display_name

class Status(models.Model):
    status_name = models.CharField(max_length=250)
    status_grievance = models.ForeignKey(Grievance,on_delete=models.CASCADE)
    status_active = models.BooleanField(default=False)

    def __str__(self):
        return self.status_name



# Create your models here.
