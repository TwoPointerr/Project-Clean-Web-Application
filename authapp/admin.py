from django.contrib import admin
from authapp.models import Post, User,CitizenProfile,MCProfile,Location
admin.site.register([User,Post,CitizenProfile,MCProfile,Location])
# Register your models here.
