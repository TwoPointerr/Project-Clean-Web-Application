from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from api.serializers import GrievanceDisplaySerializer
from grievance_data.models import Grievance

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def grievance_display(request,*args, **kwargs):
    grievance_all_obj = Grievance.objects.all()
    gri_serializer = GrievanceDisplaySerializer(grievance_all_obj,many=True)
    return Response(data={"gri_data":gri_serializer.data})

# Create your views here.
