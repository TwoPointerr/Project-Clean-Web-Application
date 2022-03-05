from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(verbose_name='email',max_length=255,unique=True)
    phone = models.CharField(null=True, max_length=255)
    isMcUser = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['first_name','last_name','username']
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

class Location(models.Model):
    loc_lat = models.FloatField()
    loc_long = models.FloatField()
    loc_display_name = models.TextField()
    loc_suburb = models.CharField(max_length=250)
    loc_city = models.CharField(max_length=250)
    loc_municipality = models.TextField()
    loc_state_distric = models.CharField(max_length=250)
    loc_state = models.CharField(max_length=250)
    loc_postcode = models.PositiveIntegerField()

    def __str__(self):
        return self.loc_suburb

class MCProfile(models.Model):
    mc_user = models.OneToOneField(User,on_delete=models.CASCADE)
    mc_profile_img = models.ImageField(default='profiles_pics/default.jpg',upload_to="profiles_pics",blank=True)
    mc_employee_id = models.CharField(max_length=250)
    mc_muncipal_co = models.TextField()
    mc_location = models.OneToOneField(Location,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.mc_user.first_name


class Post(models.Model):
    title = models.CharField(null= True,max_length=255)
    post_img = models.ImageField(upload_to="products",blank=True)