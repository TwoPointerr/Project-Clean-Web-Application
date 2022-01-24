from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from authapp.models import User
from dashboard.models import Desk
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html')

def colorDemo(request):
    desk = Desk.objects.all()
    return render(request,'muncipalDashboard.html',{"desk":desk})

def workSpace(request):
    return render(request,"WorkspaceDashboard.html")

def searchDemo(request):
    return render(request,'search-results.html')

def getDeskInfo(request):
    desk = Desk.objects.all()
    data = serializers.serialize('json',desk)
    return HttpResponse(data, content_type='application/json')
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
            first_name=firstname, last_name=lastname, username=username, email=email, password=password)
        user.save()
        login(request, user)
        return redirect("dashboard:search")
    
    return render(request,'sign-up.html')

def accountDetail(request):
    return render(request,'account-detail.html')

def accountSetting(request):
    return render(request,'account-setting.html')
    