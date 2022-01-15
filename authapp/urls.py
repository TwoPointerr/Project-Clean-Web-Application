from django.urls import path, include
from authapp import views

urlpatterns = [ 
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('get_data', views.get_data),
    path('get_all_users',views.get_all_user),
    path('upload_post',views.PostCreate.as_view())
]