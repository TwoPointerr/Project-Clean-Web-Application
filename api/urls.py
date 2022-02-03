from django.urls import path, include
from api import views 

urlpatterns = [
    path("get-gri-data/",views.grievance_display,name="get-gri-data")
]