from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages


# Create your views here.

def loginn(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            messages.info(request,"you logged in ")
            #return redirect('sup')
            #login(request,user)
            #return redirect('sin')
        else:
            messages.error(request,'username or password not correct')
            return redirect('lin')

    return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if User.objects.filter(username=uname).exists():
            messages.info(request, "username taken")
            return redirect('sup')
        elif User.objects.filter(email=email).exists():
            messages.info(request, "email taken")
            return redirect('sup')
        

        if pass1!=pass2:
            messages.info(request, "password mismatch")
            return redirect('sup')
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('lin')
        
    return render(request,'signup.html')
