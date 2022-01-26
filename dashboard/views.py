from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from authapp.models import MCProfile, User, Location
from grievance_data.models import Grievance, Category, Status
from dashboard.models import Desk, Folders
from django.contrib.auth import authenticate, login, logout
from django.db.models import Count, Min, Sum, Avg, Max
from django.contrib import messages
from django.http import HttpResponse
from django.core import serializers
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# Create your views here.
@login_required
def muncipalDashboard(request):
    return render(request,'Muncipal Dashboard/muncipalDashboard.html',grievancesDataModels(request))
    
@login_required
def workSpace(request):
    return render(request,"Work Space/WorkspaceDashboard.html",grievancesDataModels(request))

@login_required
def grievance(request):
    return render(request,'grievance-detail.html')

def signin(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
        password = request.POST.get('password')
        # user = authenticate(username= email, password= password)
        user = auth.authenticate(email = mail, password = password)
        if user is not None:
            login(request, user)
            messages.info(request,'Logged in')
            return redirect("dashboard:muncipal_dashboard")
            
        else:
            messages.warning(request,'Username and Password mismatch.')
            return redirect("dashboard:signin")
    return render(request,'Account/sign-in.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        email = request.POST.get('mail')
        username = request.POST.get('mail')
        password = request.POST.get('password')
        user = User.objects.create_user(
            first_name=firstname, last_name=lastname, username=username, email=email, password=password, isMcUser =True)
        user.save()
        MCProfile.objects.create(mc_user=user)
        login(request, user)
        messages.info(request,'Enter Account Details.')
        return redirect("dashboard:acsetting")
    return render(request,'Account/sign-up.html')

@login_required
def accountSetting(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    profile = MCProfile.objects.get(mc_user=user)
    previmg=profile.mc_profile_img
    if request.user.is_authenticated:
        if request.method == 'POST':

            user.first_name = request.POST.get('fname')
            user.last_name = request.POST.get('lname')
            user.email = request.POST.get('mail')
            user.save(update_fields=['first_name', 'last_name'])

            profile.mc_employee_id = request.POST.get('empid')
            profile.mc_muncipal_co = request.POST.get('city')
            profile.mc_profile_img = request.FILES.get('img')
            
            newimg=profile.mc_profile_img
            
            if str(newimg) == '':
               profile.mc_profile_img = previmg                     

            profile.save(update_fields=['mc_employee_id', 'mc_muncipal_co', 'mc_profile_img'])
            messages.success(request,'Information Updated.')
            return redirect("dashboard:muncipal_dashboard")
    else:
        messages.warning(request,'You are not signed in.')
        return redirect("dashboard:signin")
    return render(request,'Account/account-setting.html', {'profile': profile, 'user': user})

@login_required
def signout(request):
    logout(request)
    messages.info(request,'Logged Out Successfully.')
    return redirect("dashboard:signin")


#AJAX Function return JSON Response

def createDesk(request):
    mc_profile = MCProfile.objects.get(mc_user=request.user)
    desk_name = str(request.GET.get('desk_name'))
    desk = Desk.objects.create(desk_mc_user=mc_profile,desk_name=desk_name)
    print(desk)
    return JsonResponse({'data':"succesful"})

def createFolder(request):
    desk_id = int(request.GET.get('desk_id').split("_")[1])
    desk = Desk.objects.get(id=desk_id)

    folder_name = str(request.GET.get('folder_name'))
    folder = Folders.objects.create(folder_desks=desk,folder_name=folder_name)

    return JsonResponse({'data':'successful'})

def displayDeskList(request):
    mc_profile = MCProfile.objects.get(mc_user=request.user)
    desks = Desk.objects.filter(desk_mc_user=mc_profile)
    template = render_to_string('Work Space/desksList.html', {'desk_list': desks})
    return JsonResponse({'data':template})

def displayDeskFolders(request):
    desk_id = int(request.GET.get('desk_id').split("_")[1])
    desk = Desk.objects.get(id=desk_id)
    template = render_to_string('Work Space/DeskFolderList.html', {'desk_single': desk})
    return JsonResponse({'data':template})

def getDeskInfo(request):
    desk_id = int(request.GET.get('desk_id').split("_")[1])
    desk = Desk.objects.get(id=desk_id)
    template = render_to_string('Base HTML/modalFolderTemplate.html', {'desk_single': desk})
    return JsonResponse({'data':template})

def loadDesk(request):
    mc_profile = MCProfile.objects.get(mc_user=request.user)
    desk_id = int(request.GET.get('desk_id').split("_")[1])
    desk = Desk.objects.get(id=desk_id)
    dataDict = grievancesDataModels(request)
    dataDict['desk_single'] = desk
    template = render_to_string('Work Space/insideDesk.html', dataDict)
    return JsonResponse({'data':template})

def filter_data(request):
    grievance_all_list = Grievance.objects.all()
    grievance_list = filter_data_functionality(request,grievance_all_list)
    template = render_to_string('ajax/grievance-list.html', {'grievance_list': grievance_list})
    print("inside filter data")
    return JsonResponse({'data':template})

#Supporting Functions

#Return Dict with Gri Model
def grievancesDataModels(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    profile = MCProfile.objects.get(mc_user=user)
    grievance = Grievance.objects.all()
    category =Category.objects.all()
    minvote = Grievance.objects.all().aggregate(Min('gri_upvote'))['gri_upvote__min']
    maxvote = Grievance.objects.all().aggregate(Max('gri_upvote'))['gri_upvote__max']
    status = Status.objects.values_list('status_name',flat=True).distinct()
    location = Location.objects.all().distinct('loc_city')
    return {'grievances':grievance, 'category':category,'minVote':minvote,'maxVote':maxvote,'status':status,'location':location, 'profile':profile}

#Filter Gri Model and return Gri model OBJ
def filter_data_functionality(request,grievance_list):
    min_vote = request.GET.get('minVote')
    max_vote = request.GET.get('maxVote')
    grievance_list = grievance_list.filter(gri_upvote__gte=min_vote).order_by('gri_upvote')
    grievance_list = grievance_list.filter(gri_upvote__lte=max_vote).order_by('gri_upvote')
    
    gri_categories= request.GET.getlist('grievance_category[]')
    category = Category.objects.filter(cat_name__in=gri_categories)
    
    if len(gri_categories)>0:
        grievance_list = grievance_list.filter(gri_category_id__in=category)
    
    gri_status= request.GET.getlist('grievance_status[]')
    stat = Status.objects.filter(status_active=True).filter(status_name__in=gri_status).distinct('status_grievance')
    
    if len(gri_status)>0:
        grievance_list = grievance_list.filter(status__in=stat)
    
    griloc= request.GET.getlist('grievance_location[]')
    location = Location.objects.filter(loc_city__in=griloc)
    if len(gri_status)>0:
        grievance_list = grievance_list.filter(gri_location_id__in=location)
    
    sort_by_categories= request.GET.getlist('sort_by[]')
    if len(sort_by_categories)>0:
        if(sort_by_categories[0] == 'l_h_sort_by'):
            grievance_list = grievance_list.all().order_by('gri_upvote')
        elif(sort_by_categories[0] == 'h_l_sort_by'):
            grievance_list = grievance_list.all().order_by('-gri_upvote')
        elif(sort_by_categories[0] == 'o_sort_by'):
            grievance_list = grievance_list.all().order_by('gri_timeStamp')
        elif(sort_by_categories[0] == 'l_sort_by'):
            grievance_list = grievance_list.all().order_by('-gri_timeStamp')
    
    return grievance_list
