from django.contrib import admin
from authapp.models import Post, User
admin.site.register([User,Post])
# Register your models here.
