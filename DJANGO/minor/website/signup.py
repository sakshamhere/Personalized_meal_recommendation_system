# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib import messages
from .models import Profile
import os
import pandas as pd
#from django.contrib import messages

def signup_user(request):
    if request.method=='POST':
         fname = request.POST.get('fname', 'default')
         lname = request.POST.get('lname', 'default')
         number = request.POST.get('number', 'default')  
         email = request.POST.get('email', 'default')
         passw = request.POST.get('passw', 'default')
         re_pass = request.POST.get('re_pass', 'default')
         
         if len(fname)<3 or fname.isnumeric():
             messages.error(request,"First Name should be string with more than 2 character")
             return render(request,'website/signup.html')
         if len(lname)<3 or lname.isnumeric():
             messages.error(request,"Last Name should be string with more than 2 character")
             return render(request,'website/signup.html')
         if len(passw)<5:
             messages.error(request,'Length of password must be greater or equal to 5')
             return render(request,'website/signup.html')
         if passw.isalnum()==False:
             messages.error(request,'Password must be alphanumeric')
             return render(request,'website/signup.html')
         elif(passw != re_pass):
             messages.error(request, 'Error! Password does not match')
             return render(request,'website/signup.html')
         elif len(number)!=10:
             messages.error(request, 'Error! Number must contain 10 digits')
             return render(request,'website/signup.html')
         else:
             try:
                 myuser= User.objects.get(username=number)
                 if(myuser.username==number):
                     messages.error(request,' Number :- '+myuser.username+' already exist ! Please use another number')
                     return render(request, 'website/signup.html')
             except User.DoesNotExist:
                 myuser=User.objects.create_user(number,email,passw)
                 myuser.first_name =fname
                 myuser.last_name = lname
                 myuser.save()
                 #messages.success(request, 'Registered Successfully')
                 params={'name' : fname+" "+lname,'number':number, 'email':email}
                 user=authenticate(username=number,password=passw)
                 login(request,user)
                 messages.success(request,"User created successfully, Now please complete your profile")
                 return render(request,'website/profile.html',params)
    else:
        return render(request,'website/signup.html')
         
         
  
def fill_CSV(user,lst):
    
    filename=r'C:\Users\MMG\Desktop\NBMRS\minor\website\csvfile\user_Profiles.csv'
    df=pd.read_csv(filename)  
    
    if user in df.values:     #user is variable for user
        df=df.set_index('User_Id')
        df=df.drop(user,axis=0)
        df=df.reset_index()
        df=df.append(pd.Series(lst,index=df.columns),ignore_index=True) #lst = values in list which we want to insert
        os.remove(filename)
        df.to_csv(filename,index=False)
    else:
        df=df.append(pd.Series(lst,index=df.columns),ignore_index=True) #lst = values in list which we want to insert
        os.remove(filename)
        df.to_csv(filename,index=False)        
      
    

def create_profile(request):
    if request.method=='POST' and request.FILES['image']:
        image = request.FILES['image']
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        blood = request.POST.get('blood')
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        favfood = request.POST.get('favfood')
        ft = request.POST.getlist('food')
        foodtype="++".join(ft)
        
        dt = request.POST.getlist('diet')
        diet="++".join(dt)
        
        cs = request.POST.getlist('cuisines')
        cuisines = '++'.join(cs) 
        
        nrt = request.POST.getlist('nutrient')
        nutrient = '++'.join(nrt)
        
        des = request.POST.getlist('disease')
        disease='++'.join(des)
        
        medicalhistory=request.POST.get('medicalHistory')
        
        
        prfl=Profile(name=name,email=email,number=number,gender=gender,age=age,blood=blood,weight=weight
                     ,height=height,favfood=favfood,foodtype=foodtype,diet=diet,nutrient=nutrient,
                     cuisines=cuisines,disease=disease,medicalhistory=medicalhistory,image=image)
        prfl.save()
        
        fill_CSV(request.user.username,[request.user.username," ".join(ft),nutrient.replace("++"," "),disease.replace("++"," "),diet.replace("++"," ")])      
        
        messages.success(request,'Profile created successfully')
        return redirect('Home')
    else:
        try:
            img= Profile.objects.get(number=request.user.username).image.url
        except:
            img=""
        return render(request,'website/profile.html',{'image':img})