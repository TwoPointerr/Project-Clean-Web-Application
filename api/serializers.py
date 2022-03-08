from dataclasses import field
from statistics import mode
from rest_framework import serializers
from grievance_data.models import Grievance, Category
from authapp.models import Location, CitizenProfile
from authapp.serializers import UserDisplaySrializer, CitizenDisplaySerializer
from geopy.geocoders import Nominatim

class LocationCreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        loc_long = validated_data.get('loc_long')
        loc_lat = validated_data.get('loc_lat')
        locationDict = getLocationDetails(loc_long,loc_lat)
        print(locationDict)
        location = Location.objects.create(**locationDict)
        return location

    class Meta:
        model = Location
        fields = ('id','loc_long', 'loc_lat','loc_display_name','loc_suburb','loc_city','loc_municipality','loc_state_distric','loc_state','loc_postcode')
        read_only_fields = ('id','loc_display_name','loc_suburb','loc_city','loc_postcode','loc_municipality','loc_state_distric','loc_state')

class CategoryDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','cat_name','cat_value')

class LocationDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id','loc_long', 'loc_lat','loc_display_name','loc_suburb','loc_city','loc_postcode')

class GrievanceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grievance
        fields = (
            "id",
            "gri_title",
            "gri_img",
            "gri_desc",
            "gri_category",
            "gri_upvote",
            "gri_priority",
            "gri_uploaded_user",
            "gri_location",
            "gri_timeStamp")
        read_only_fields = ("gri_timeStamp",)
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        # self.fields["gri_category"] = CategoryDisplaySerializer(instance.gri_category).data
        # self.fields["gri_uploaded_user"] = CitizenDisplaySerializer(instance.gri_uploaded_user).data
        # self.fields["gri_location"] = LocationDisplaySerializer(instance.gri_location).data
        response["gri_category"] = CategoryDisplaySerializer(instance.gri_category).data
        response["gri_uploaded_user"] = CitizenDisplaySerializer(instance.gri_uploaded_user).data
        response["gri_location"] = LocationDisplaySerializer(instance.gri_location).data
        return response
# Supporting  function

class GrievanceDisplaySerializer(serializers.ModelSerializer):
    gri_location = LocationDisplaySerializer()
    gri_uploaded_user = CitizenDisplaySerializer()
    gri_category = CategoryDisplaySerializer()
    class Meta:
        model = Grievance
        fields = "__all__"

def getLocationDetails(long, lat):
    geolocator = Nominatim(user_agent="geoapiExercises")
    geoLocation = geolocator.reverse(str(lat)+","+str(long))
    print(geoLocation)
    address = geoLocation.raw['address']

    loc_display_name = geoLocation.raw.get('display_name')
    loc_suburb = address.get('suburb')
    loc_city = address.get('city')
    loc_municipality = address.get('municipality')
    loc_state_distric = address.get('state_district')
    loc_state = address.get('state')
    loc_postcode = int(address.get('postcode').replace(" ", ""))

    locationDict = {'loc_long': long,
                    'loc_lat': lat,
                    'loc_display_name': loc_display_name,
                    'loc_suburb': loc_suburb,
                    'loc_city': loc_city,
                    'loc_municipality': loc_municipality,
                    'loc_state_distric': loc_state_distric,
                    'loc_state': loc_state,
                    'loc_postcode': loc_postcode}
    
    return locationDict