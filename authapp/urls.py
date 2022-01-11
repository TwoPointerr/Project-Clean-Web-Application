from django.urls import path, include
from authapp import views

urlpatterns = [ 
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('get_data', views.get_data)
]