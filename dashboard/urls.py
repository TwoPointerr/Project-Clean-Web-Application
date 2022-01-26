
from django.urls import path, include
from dashboard import views

app_name="dashboard"
urlpatterns = [

    path('signin/', views.signin, name="signin"),
    path('register/', views.register, name="register"),
    # path('acdetail/', views.accountDetail, name="acdetail"),
    path('acsetting/', views.accountSetting, name="acsetting"),

    path('',views.muncipalDashboard,name="muncipal_dashboard"),
    path('workspace/',views.workSpace, name="workspace"),

    path('grievance',views.grievance, name="grievance"),

    #JSON Response AJAX
    path('getDeskInfo/',views.getDeskInfo),
    path('loadDesk/',views.loadDesk,name="loadDesk"),

    path('filter-data/', views.filter_data, name="filter_data"),
]
