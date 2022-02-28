from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from api.serializers import GrievanceCreateSerializer, GrievanceDisplaySerializer, getLocationDetails
from grievance_data.models import Grievance
from authapp.models import Location
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def grievance_display(request,*args, **kwargs):
    # loc_long = request.data['loc_long']
    # loc_lat = request.data['loc_lat']
    # loc_suburb = [getLocationDetails(loc_long,loc_lat)['loc_suburb']]
    # location = Location.objects.filter(loc_suburb__in=loc_suburb)
    # print(location)
    # grievance_all_obj = Grievance.objects.filter(gri_location_id__in=location)
    grievance_all_obj = Grievance.objects.all()
    gri_serializer = GrievanceDisplaySerializer(grievance_all_obj,many=True)
    return Response(data={"gri_data":gri_serializer.data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_gri(request,*args, **kwargs):
    loc_long = request.data.pop('loc_long')[0]
    loc_lat = request.data.pop('loc_lat')[0]
    locationDict = getLocationDetails(loc_long,loc_lat)
    location = Location.objects.create(**locationDict)
    request.data.update({"gri_location":location.id})
    gri_serializer = GrievanceCreateSerializer(data=request.data)
    if gri_serializer.is_valid():
        gri_serializer.save()
        return Response(data={"status":f"{status.HTTP_200_OK}",},status=status.HTTP_200_OK)
    else:
        return Response(data={"status":f"{gri_serializer.errors}",},status=status.HTTP_200_OK)