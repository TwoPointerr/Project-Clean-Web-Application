
from django.urls import path, include
from dashboard import views

app_name="dashboard"
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('signin/', views.signin, name="signin"),
    path('register/', views.register, name="register")
]
