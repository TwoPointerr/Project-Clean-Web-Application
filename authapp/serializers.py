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
        fields = ('id', 'email', 'username','first_name', 'last_name','phone')

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email', 'username','first_name', 'last_name', 'phone')

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def validate_username(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})
        return value

    def update(self, instance, validated_data):
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']
        instance.username = validated_data['username']

        instance.save()

        return instance

class CitizenDisplaySerializer(serializers.ModelSerializer):
    citi_user = UserDisplaySrializer()
    class Meta:
        model = CitizenProfile
        fields = ("id","citi_user","citi_profile_img")

class Citizen_CU_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CitizenProfile
        fields = ("citi_user","citi_profile_img")
        
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["citi_user"] = UserDisplaySrializer(instance.citi_user).data
        return response

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'post_img')



