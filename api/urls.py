from unicodedata import name
from django.urls import path, include
from api import views 

urlpatterns = [
    path("get-gri-data/",views.grievance_display,name="get-gri-data"),
    path("upload-gri/",views.create_gri,name="upload-data"),

    path("upvote-gri/",views.upvote_grievance,name="upvote-gri"),
    path("get-severity/",views.get_severity,name="get-severity") #temprary delete later

]