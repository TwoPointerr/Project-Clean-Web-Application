
from django.urls import path, include
from dashboard import views

app_name="dashboard"
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('signin/', views.signin, name="signin"),
    path('register/', views.register, name="register"),
    path('acdetail/', views.accountDetail, name="acdetail"),
    path('acsetting/', views.accountSetting, name="acsetting"),
    path('muncipal-dashboard',views.muncipalDashboard,name="muncipal_dashboard"),
    path('workspace/',views.workSpace, name="workspace"),
    path('search',views.searchDemo, name="search"),
    path('getDeskInfo/',views.getDeskInfo),
    path('loadDesk/',views.loadDesk,name="loadDesk"),
    path('search',views.searchDemo, name="search"),
    path('grievance',views.grievance, name="grievance")
    
]
