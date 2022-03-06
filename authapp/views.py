from django.http import response
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from authapp import serializers
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from authapp.models import CitizenProfile, Post, User
from authapp.serializers import Citizen_CU_Serializer, UserDisplaySrializer, PostSerializer, UserUpdateSerializer, UserCreateSerializer
from api.serializers import LocationCreateSerializer

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
    serializer = PostSerializer(posts,many=True)
    return Response(data={"POsts":serializer.data})

@api_view(['POST']) #need to update later
def create_citi_profile(request, *args, **kwargs):
    citiSerializer = Citizen_CU_Serializer(data=request.data)
    if citiSerializer.is_valid():
        citiSerializer.save()
    return Response(data=citiSerializer.data)
    
@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def update_profile(request, *args, **kwargs):
    requestData = request.data.copy()
    print(requestData)
    #return Response(data={"user":"test@email.com","user_update":"Successful","citi_profile":"Successful"})

    # profile_img = requestData.pop('profile_img')[0]

    # try:
    #     user = User.objects.get(id=int(requestData['id']))
    # except User.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    
    # if request.method == 'POST':
    #     user_update_serializer = UserUpdateSerializer(user,data=requestData)
    #     if user_update_serializer.is_valid():
    #         user_update_serializer.save()
    #         return Response(data=user_update_serializer.data)
    #     else:
    #         return Response(data=user_update_serializer.errors)

    # try:
    #     citizen_obj = CitizenProfile.objects.get(citi_user=user)
    # except CitizenProfile.DoesNotExist:
    #     citizen_create_serializer = Citizen_CU_Serializer(data={"citi_user":user.id,"citi_profile_img":profile_img})
    #     if citizen_create_serializer.is_valid():
    #         citizen_create_serializer.save()
    #         citizen_obj = CitizenProfile.objects.get(citi_user=user)
        
    # if request.method == 'POST':
    #     user_update_serializer = UserCreateSerializer(user,data=requestData)
    #     if user_update_serializer.is_valid():
    #         user_update_serializer.save()
    #         citizen_profile_update_serializer = Citizen_CU_Serializer(
    #             citizen_obj,
    #             data={
    #                 "id":citizen_obj.id,
    #                 "citi_user":user_update_serializer.data['id'],
    #                 "citi_profile_img":profile_img
    #                 })
    #         if citizen_profile_update_serializer.is_valid():
    #             citizen_profile_update_serializer.save()
    #             print(str(user_update_serializer.data))
    #             return Response(data=user_update_serializer.data)
    #         else:
    #             return Response(citizen_profile_update_serializer.errors)
    #     else:
    #         return Response(user_update_serializer.errors)
    
class UpdateUser(UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserUpdateSerializer

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

class Location(APIView):
    def post(self,request, format=None):
        serializer = LocationCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Create your views here.
