from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import ValueStore
import numpy as np
import joblib
import pickle

# with open('heartproj/decision_model.sav', 'rb') as f:
#                 model = pickle.load(f)

# Create your views here.
def homepage1(request):
    return render(request, 'homepage1.html')

def homepage2(request):
    return render(request, 'homepage2.html')

def predict(request):
    if request.method=='POST':
        age=int(request.POST["age"])
        gender=int(request.POST["gender"])
        cp=int(request.POST["cp"])
        trestbps=int(request.POST["trestbps"])
        cholestrol=int(request.POST["cholestrol"])
        fbs=int(request.POST["fbs"])
        restecg=int(request.POST["restecg"])
        thalach=int(request.POST["thalach"])
        exang=int(request.POST["exang"])
        oldpeak=int(request.POST["oldpeak"])
        slope=int(request.POST["slope"])
        ca=int(request.POST["ca"])
        thal=int(request.POST["thal"])
        
        data = np.array([[age, gender, cp, trestbps, cholestrol, fbs, restecg, thalach]]) #exang, oldpeak, slope, ca, thal
        #arr = np.array(data)
        # load the trained model
        model = joblib.load("savedmodels/dt_model.pkl")
        # model = pickle.load(open('savedmodels/decision_model.sav','rb'))
        
        # predict the output for the input values
        prediction =  model.predict(data)
        
        ValueStore.objects.create(age=age,gender=gender,cp=cp,trestbps=trestbps,cholestrol=cholestrol,fbs=fbs,restecg=restecg,thalach=thalach,exang=exang,oldpeak=oldpeak,slope=slope,ca=ca,thal=thal)
        
        return render(request, 'predict.html', {'prediction': prediction})
    
    return render(request, 'predict.html')


def loginn(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            messages.info(request,"you logged in ")
            return redirect('home2')
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
