from django.urls import path, include
from grievance_data import views

urlpatterns = [ 
    path('create_grievance',views.CreateGrievance.as_view()),
]