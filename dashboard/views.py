from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from authapp.models import MCProfile, User
from grievance_data.models import Grievance, Category, Status
from dashboard.models import Desk
from django.contrib.auth import authenticate, login
from django.db.models import Count, Min, Sum, Avg, Max
from django.http import HttpResponse
from django.core import serializers
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html')

def colorDemo(request):
    desk = Desk.objects.all()
    grievance = Grievance.objects.all()
    return render(request,'muncipalDashboard.html',{'grievances':grievance})

def workSpace(request):
    return render(request,"WorkspaceDashboard.html")

def muncipalDashboard(request):
    grievance = Grievance.objects.all()
    category =Category.objects.all()
    minvote = Grievance.objects.all().aggregate(Min('gri_upvote'))['gri_upvote__min']
    maxvote = Grievance.objects.all().aggregate(Max('gri_upvote'))['gri_upvote__max']
    status = Status.objects.values_list('status_name',flat=True).distinct()
    print(status)
    return render(request,'muncipalDashboard.html',{'grievances':grievance, 'category':category,'minVote':minvote,'maxVote':maxvote,'status':status})


def searchDemo(request):
    return render(request,'search-results.html')

def getDeskInfo(request):
    desk = Desk.objects.all()
    data = serializers.serialize('json',desk)
    return HttpResponse(data, content_type='application/json')

def loadDesk(request):
    mc_profile = MCProfile.objects.get(mc_user=request.user)
    desk_id = int(request.GET.get('desk_id').split("_")[1])
    desk = Desk.objects.get(id=desk_id)
    template = render_to_string('insideDesk.html', {'desk_single': desk})
    return JsonResponse({'data':template})

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
            return redirect("dashboard:acdetail")
            
        else:
            return redirect("dashboard:register")
    return render(request,'sign-in.html')



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
        return redirect("dashboard:acsetting")
    
    return render(request,'sign-up.html')

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
            # messages.success(request,'Information Added.')
            return redirect("dashboard:searchDemo")
    else:
        # messages.warning(request,'You are not signed in.')
        return redirect("dashboard:signin")
    return render(request,'account-setting.html', {'profile': profile, 'user': user})




def filter_data(request):
    grievance_all_list = Grievance.objects.all()
    grievance_list = filter_data_functionality(request,grievance_all_list)
    template = render_to_string('ajax/grievance-list.html', {'grievance_list': grievance_list})
    return JsonResponse({'data':template})



    
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
    
    # grievance_sort_list = grievance_sort_list.all().order_by('title')
    # if len(sub_categories)>0:
    #     grievance_list = grievance_list.filter(sub_cat__in=sub_categories)
    # if len(article_categories)>0:
    #     grievance_list = grievance_list.filter(articel_type__in=article_categories)
    
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
        # grievance_list = grievance_list.all().order_by('title')
    # if len(color_filter)>0:
    #     grievance_list = grievance_list.filter(color__in=color_filter)
    # if len(grievance_brands)>0:
    #     # category = Category.objects.filter(title__in=categories)
    #     grievance_list = grievance_list.filter(brand__in=grievance_brands)
    
    return grievance_list
