from dataclasses import field
from statistics import mode
from rest_framework import serializers
from grievance_data.models import Grievance, Category
from authapp.models import Location
from authapp.serializers import UserDisplaySrializer, CitizenDisplaySerializer
from geopy.geocoders import Nominatim

class LocationSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        loc_long = validated_data.get('loc_long')
        loc_lat = validated_data.get('loc_lat')
        locationDict = getLocationDetails(loc_long,loc_lat)
        print(locationDict)
        location = Location.objects.create(**locationDict)
        return location

    class Meta:
        model = Location
        fields = ('loc_long', 'loc_lat')

class CategoryDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('cat_name',)

class LocationDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"

class GrievanceDisplaySerializer(serializers.ModelSerializer):
    gri_location = LocationDisplaySerializer()
    gri_uploaded_user = CitizenDisplaySerializer()
    gri_category = CategoryDisplaySerializer()
    class Meta:
        model = Grievance
        fields = ("id","gri_img","gri_desc","gri_category","gri_upvote","gri_priority","gri_uploaded_user","gri_location","gri_timeStamp")


# Supporting  function
def getLocationDetails(long, lat):
    geolocator = Nominatim(user_agent="geoapiExercises")
    geoLocation = geolocator.reverse(str(lat)+","+str(long))
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