from django.shortcuts import render
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from authapp import serializers

from authapp.models import User
from authapp.serializers import UserDisplaySrializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_data(request, *args, **kwargs):
    return Response(data="this is my data")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_user(request, *args, **kwargs):
    users = User.objects.all()
    serializer = UserDisplaySrializer(users,many=True)
    return Response(data={"userdata":serializer.data})


# Create your views here.
