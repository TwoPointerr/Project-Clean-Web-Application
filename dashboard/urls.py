
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

    path('display-desk-cont/',views.displayDeskList,name="display-desk-cont"),
    path('display-desk-folders/',views.displayDeskFolders,name="display-desk-folders"),

    path('create-desk/',views.createDesk,name="create-desk"),
    path('create-folder/',views.createFolder,name="create-desk"),
    
    path('filter-data/', views.filter_data, name="filter_data"),
]
