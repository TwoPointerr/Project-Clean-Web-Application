from pyexpat import model
from django.forms import fields, models
from rest_framework import serializers
from grievance_data.models import Grievance, Category, Status
from authapp.models import User, CitizenProfile, MCProfile, Location
from rest_framework.authtoken.models import Token
from authapp.serializers import UserDisplaySrializer
from api.serializers import LocationCreateSerializer, getLocationDetails


#gri_img = models.ImageField(upload_to="grievance_pics")
#gri_title = models.CharField(max_length=250)
#gri_desc = models.TextField(null=True)
# ** gri_category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
#gri_upvote = models.PositiveIntegerField(default=0)
# gri_severity = models.IntegerField() // need to hadle at server side
# gri_priority = models.IntegerField() //
# ** gri_uploaded_user = models.ForeignKey(CitizenProfile,on_delete=models.CASCADE)
# ** gri_location = models.OneToOneField(Location,on_delete=models.SET_NULL,null=True)
# (auto)gri_timeStamp = models.DateTimeField(auto_now_add=True)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class grievanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grievance
        fields = '__all__'


# class grievanceSerializer(serializers.ModelSerializer):
#     # gri_location = LocationSerializer()
#     # gri_uploaded_user = UserDisplaySrializer()
#     # gri_category = CategorySerializer()

#     # gri_location = LocationSerializer()
#     #gri_uploaded_user = serializers.PrimaryKeyRelatedField(queryset=CitizenProfile.objects.all())
#     # gri_category = CategorySerializer()


#     def create(self, validated_data):
#         user_token = validated_data.pop('gri_uploaded_user')
#         print("inside serializer",user_token)
#         token = Token.objects.get(key=user_token)
#         user = User.objects.get(id=token.user_id)

#         category_json = validated_data.pop('gri_category')
#         category = Category.objects.create(**category_json)

#         gri_severity = 10

#         location_json = validated_data.pop('gri_location')
#         loc_long = location_json.get('loc_long')
#         loc_lat = location_json.get('loc_lat')

#         gri_location = Location.objects.create(
#             **getLocationDetails(loc_long, loc_lat))

#         grievance = Grievance.objects.create(gri_uploaded_user=user,
#                                              gri_category=category,
#                                              gri_severity=gri_severity,
#                                              gri_location=gri_location,
#                                              **validated_data)

#         return grievance

#     class Meta:
#         model = Grievance
#         exclude = ('gri_img','gri_severity')
