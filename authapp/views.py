from django.shortcuts import render
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from authapp import serializers
from rest_framework.views import APIView
from authapp.models import Post, User
from authapp.serializers import UserDisplaySrializer, PostSerializer

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
    
@api_view(['GET'])
def get_post(request, *args, **kwargs):
    posts = Post.objects.all()
    serializer = PostSerializer(posts)
    return Response(data={"POsts":serializer.data})

class PostCreate(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
