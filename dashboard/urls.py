
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
    path('display-modal-folder-list/',views.display_Modal_Folder_list),
    
    #used in two way for workspace nad for modal
    path('display-desks-list/',views.displayDeskList,name="display-desks-list"),
    path('workspace-inside-desk/',views.workspace_inside_desk,name="loadDesk"),

    path('display-workspace-desk-folders/',views.display_WorkSpace_DeskFolders,name="display-desk-folders"),

    path('create-desk/',views.createDesk,name="create-desk"),
    path('create-folder/',views.createFolder,name="create-desk"),
    
    path('filter-data/', views.filter_data, name="filter_data"),
]
