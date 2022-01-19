from django.db.models import fields
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = ('id','email','username','password','first_name','last_name','phone')

class UserDisplaySrializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','username')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','post_img')