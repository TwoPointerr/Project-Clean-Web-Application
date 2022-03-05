from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from api.serializers import GrievanceCreateSerializer, GrievanceDisplaySerializer, getLocationDetails
from grievance_data.models import Grievance
from authapp.models import CitizenProfile, Location, User
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from ml_models.ml_functions import gri_priority, gri_severity

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def grievance_display(request,*args, **kwargs):
#     loc_long = request.data['loc_long']
#     loc_lat = request.data['loc_lat']
#     loc_suburb = [getLocationDetails(loc_long,loc_lat)['loc_suburb']]
#     location = Location.objects.filter(loc_suburb__in=loc_suburb)
#     print(location)
#     grievance_all_obj = Grievance.objects.filter(gri_location_id__in=location)
#     #grievance_all_obj = Grievance.objects.all()
#     gri_serializer = GrievanceDisplaySerializer(grievance_all_obj,many=True)
#     return Response(data={"gri_data":gri_serializer.data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upvote_grievance(request,*args, **kwargs):
    user = User.objects.get(id=int(request.data['user_id']))
    citi_user = CitizenProfile.objects.get(citi_user=user)
    gri_obj = get_object_or_404(Grievance,id=int(request.data['gri_id']))
    gri_obj.gri_upvote_list.add(citi_user)
    gri_obj.gri_upvote=gri_obj.gri_upvote_list.all().count()
    gri_obj.save()
    return Response(data={"gri_id":request.data['user_id'],"gri_title":f"{gri_obj.gri_title}","gri_upvotes":gri_obj.gri_upvote})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def grievance_display(request,*args, **kwargs):
    # loc_long = request.data['loc_long']
    # loc_lat = request.data['loc_lat']
    # loc_suburb = [getLocationDetails(loc_long,loc_lat)['loc_suburb']]
    # location = Location.objects.filter(loc_suburb__in=loc_suburb)
    # print(location)
    # grievance_all_obj = Grievance.objects.filter(gri_location_id__in=location)
    grievance_all_obj = Grievance.objects.all().order_by('-gri_timeStamp')
    gri_serializer = GrievanceDisplaySerializer(grievance_all_obj,many=True)
    return Response(data={"gri_data":gri_serializer.data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_gri(request,*args, **kwargs):
    requestData = request.data.copy() 
    print(requestData)
    loc_long = requestData.pop('loc_long')[0]
    loc_lat = requestData.pop('loc_lat')[0]
    uploaded_user = User.objects.get(id=int(requestData.pop('gri_uploaded_user')[0]))
    citiProfile = CitizenProfile.objects.get(citi_user=uploaded_user)
    locationDict = getLocationDetails(loc_long,loc_lat)
    location = Location.objects.create(**locationDict)
    requestData.update({"gri_location":location.id,"gri_uploaded_user":citiProfile.id})
    gri_serializer = GrievanceCreateSerializer(data=requestData)
    if gri_serializer.is_valid():
        gri_serializer.save()
        gri_obj = Grievance.objects.get(id=gri_serializer.data['id'])
        gri_obj.gri_severity = gri_severity(gri_obj.gri_img,gri_obj.gri_category.cat_name)
        gri_obj.gri_priority = gri_priority(gri_obj)
        gri_obj.save()
        return Response(data=gri_serializer.data,status=status.HTTP_200_OK)
    else:
        return Response(gri_serializer.errors)
    #return Response(data={"status":"OK"})

@api_view(['GET'])
def get_severity(request,*args, **kwargs):
    gri_obj = Grievance.objects.get(id=4)
    priority = gri_priority(gri_obj)
    severity = gri_severity(gri_obj.gri_img,"Garbage")
    return Response(data={"severity":severity,"priority":priority,"gri_bj":str(gri_obj)})


    
