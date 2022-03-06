from django.urls import path, include
from authapp import views
appname = 'authapp'
urlpatterns = [ 
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('update-user/<int:pk>',views.UpdateUser.as_view(),name="update-profile"),
    path('create-citi-profile',views.create_citi_profile,name="create-citi-profile"),
    
    path('get_data', views.get_data),
    path('get_all_users',views.get_all_user),
    path('upload_post',views.PostCreate.as_view()),
    path('get_post',views.get_post),
    path('location',views.Location.as_view()),
]