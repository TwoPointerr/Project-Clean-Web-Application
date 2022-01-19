from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from authapp.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def dashboard(request):

    return render(request,'dashboard.html')


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
    return render(request,'signin.html')



def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('mail')
        username = request.POST.get('mail')
        password = request.POST.get('password')

        user = User.objects.create_user(
            first_name=firstname, last_name=lastname, username=username, email=email, password=password)
        user.save()
        login(request, user)
        return redirect("dashboard:dashboard")
    
    return render(request,'register.html')


    