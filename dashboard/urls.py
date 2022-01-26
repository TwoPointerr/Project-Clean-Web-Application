
from django.urls import path, include
from dashboard import views

app_name="dashboard"
urlpatterns = [

    path('signin/', views.signin, name="signin"),
    path('register/', views.register, name="register"),
    path('acsetting/', views.accountSetting, name="acsetting"),
    path('signout/',views.signout, name="signout"),

    path('',views.muncipalDashboard,name="muncipal_dashboard"),
    path('workspace/',views.workSpace, name="workspace"),

    path('grievance',views.grievance, name="grievance"),

    #JSON Response AJAX
    path('getDeskInfo/',views.getDeskInfo),
    path('loadDesk/',views.loadDesk,name="loadDesk"),

    path('filter-data/', views.filter_data, name="filter_data"),
]
