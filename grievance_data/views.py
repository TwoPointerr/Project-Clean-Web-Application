from rest_framework.views import APIView
from grievance_data.serializers import grievanceSerializer
from rest_framework.response import Response
from grievance_data.models import Grievance

class CreateGrievance(APIView):
    def get(self,request):
        gri = Grievance.objects.all()
        gri_serializer = grievanceSerializer(gri,many=True)
        return Response(gri_serializer.data)
    def post(self,request, format=None):
        #serializer = grievanceSerializer(data=request.data)
        
        return Response({str(request.data)})
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data,status=status.HTTP_200_OK)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
