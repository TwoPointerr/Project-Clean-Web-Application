from statistics import mode
from django.db import models
from authapp.models import User,MCProfile
from grievance_data.models import Grievance

class Desk(models.Model):
    desk_name = models.CharField(max_length=250)
    desk_mc_user = models.ForeignKey(MCProfile,on_delete=models.CASCADE)
    desk_gri_files = models.ManyToManyField(Grievance)

    def __str__(self) -> str:
        return self.desk_name


class Folders(models.Model):
    folder_desks = models.ForeignKey(Desk,on_delete=models.CASCADE,blank=True,default="")
    folder_name = models.CharField(max_length=250)
    folder_gri_file = models.ManyToManyField(Grievance)

    def __str__(self) -> str:
        return self.folder_name


# Create your models here.
