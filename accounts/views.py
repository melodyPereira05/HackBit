from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.


def login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.add_message(request, messages.SUCCESS, 'You have now logged in successfully')
            return redirect('accounts:dashboard-profile')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Credentials')
            return redirect('accounts:login')
   
    else:
        return render(request,'login.html')
   
   


def register(request):
    if request.method =='POST':
        # messages.add_message(request, messages.ERROR, 'Username taken')
        # return redirect('register')
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST.get('username')
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.add_message(request, messages.ERROR, 'Username taken')
                return redirect('accounts:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.add_message(request, messages.ERROR, 'Email Already Exist')
                    return redirect('accounts:register')
                else:
                    user=User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
                    user.save()
                    messages.add_message(request, messages.SUCCESS, 'You are now register,please log in')
                    return redirect('accounts:login')
                
        else:
            messages.add_message(request, messages.ERROR, 'Passwords does not match')
            return redirect('accounts:register')
    
        
    return render(request,'register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS, 'You have been logged out successfullt')
        return redirect('home')
    
    return redirect('home')


def dashboardprofile(request):
    return render(request,'dashboardprofile.html')