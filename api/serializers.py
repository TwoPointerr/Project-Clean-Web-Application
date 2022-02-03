from rest_framework import serializers
from grievance_data.models import Grievance

class GrievanceDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Grievance
        fields = "__all__"