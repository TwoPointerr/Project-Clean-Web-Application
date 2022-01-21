
from django.urls import path, include
from dashboard import views

app_name="dashboard"
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('signin/', views.signin, name="signin"),
    path('register/', views.register, name="register"),
    path('acdetail/', views.accountDetail, name="acdetail"),
    path('acsetting/', views.accountSetting, name="acsetting"),
    path('colors',views.colorDemo),
    path('search',views.searchDemo, name="search"),
    path('grievance',views.grievance, name="grievance")
]
