
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

    path('grievance-detail/<int:gri_id>/',views.grievance, name="grievance-detail"),

    #JSON Response AJAX
    path('display-modal-folder-list/',views.display_Modal_Folder_list),
    
    #used in two way for workspace nad for modal
    path('display-desks-list/',views.displayDeskList,name="display-desks-list"),
    path('workspace-inside-desk/',views.workspace_inside_desk,name="workspace-inside-desk"),
    path('workspace-inside-folder/',views.workspace_inside_folder,name="workspace-inside-folder"),

    path('display-workspace-desk-folders/',views.display_WorkSpace_DeskFolders,name="display-desk-folders"),

    #move gri to folder in MoveGri.js file
    path('move-gri-to-folder/',views.move_gri_to_folder,name="move-gri-to-folder"),
    path('move-gri-to-desk/',views.move_gri_to_desk,name="move-gri-to-desk"),

    path('reject-gri/',views.reject_gri,name="move-gri-to-desk"),

    path('create-desk/',views.createDesk,name="create-desk"),
    path('create-folder/',views.createFolder,name="create-desk"),
    
    path('filter-data/', views.filter_data, name="filter_data"),
]
