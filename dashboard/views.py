from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from authapp.models import User, MCProfile
from django.contrib.auth import authenticate, login

# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html')

def colorDemo(request):
    return render(request,'muncipalDashboard.html')

def workSpace(request):
    return render(request,"WorkspaceDashboard.html")

def searchDemo(request):
    return render(request,'search-results.html')

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
            return redirect("dashboard:dashboard")
            
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
