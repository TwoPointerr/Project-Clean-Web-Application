from django.db.models import fields
from djoser.serializers import UserCreateSerializer, UserSerializer, TokenSerializer
from rest_framework import serializers
from .models import *

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password',
                  'first_name', 'last_name', 'phone')

class UserDisplaySrializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username')

class CitizenDisplaySerializer(serializers.ModelSerializer):
    citi_user = UserDisplaySrializer()
    class Meta:
        model = CitizenProfile
        fields = ("citi_user","citi_profile_img")

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'post_img')



