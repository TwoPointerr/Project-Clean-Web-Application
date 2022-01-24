from django.db.models import fields
from djoser.serializers import UserCreateSerializer, UserSerializer, TokenSerializer
from rest_framework import serializers
from .models import *
from geopy.geocoders import Nominatim


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password',
                  'first_name', 'last_name', 'phone')


class UserDisplaySrializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'post_img')


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
