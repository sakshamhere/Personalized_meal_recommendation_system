from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Contact
from .models import Profile
import os
import datetime
import pandas as pd
#from django.http import HttpResponse

def index(request):
    if request.user.is_authenticated:
        try:
            img= Profile.objects.get(number=request.user.username).image.url
        except:
            img=""
        return render(request,'website/home.html',{'image':img})
    else:
        return render(request,'website/home.html')

def about(request):
    if request.user.is_authenticated:
        try:
            img= Profile.objects.get(number=request.user.username).image.url
        except:
            img=""
        return render(request,'website/about.html',{'image':img})
    else:
        return render(request,'website/about.html')


def login_user(request):
    if request.method=='POST':
        number = request.POST.get('number', 'default')
        passw = request.POST.get('passw', 'default')
        
        if len(number)!=10:
            messages.error(request,'Number must contain 10 digits')
            
        else:
            user=authenticate(username=number,password=passw)
            if user is not None:
                login(request,user)
                messages.success(request,'Successfully Logged in')
                return redirect('Home')
            else:
                messages.error(request,'Error : Invalid Creadentials, Please try again')
                return redirect('login')
    
    return render(request,'website/login.html')


def logout_user(request):
    if request.method== 'POST':
        logout(request)
        messages.success(request,'Successfully Logged out')
        return redirect('Home')

def decider(request):
    if request.user.is_authenticated:
        v=Profile.objects.get(number=request.user.username).second_time
        if(v==False):
            return redirect('recommend')
        else:
            return redirect('SecondRecommend')
    else:
        messages.error(request,'you must be logged in for meal')
        return redirect('Home')

def contact(request):
    if request.method=='POST':
        name = request.POST.get('name', 'default')
        email = request.POST.get('email', 'default')
        number = request.POST.get('phone', 'default')  
        message = request.POST.get('message', 'default')
        
        if len(name)<3 or name.isnumeric():
            messages.error(request,"Name should be string with more than 2 character")
        elif len(number)!=10:
            messages.error(request,"Number must contain 10 digits")
        elif len(message)<10:
            messages.error(request,"Message must contain at least 25 characters")
        elif len(email)<5:
            messages.error(request,"Email must contain at least 5 character")
        else:
            contact=Contact(name=name,email=email,number=number,message=message)
            contact.save()
            messages.success(request,"your message has been sent successfuly")
            
    if request.user.is_authenticated:
        try:
            img= Profile.objects.get(number=request.user.username).image.url
        except:
            img=""
        return render(request,'website/contact.html',{'image':img})        
    else:
        return render(request,'website/contact.html')


def buy(request):
    a=request.POST.get('product_buy')
    l=list(a.split())
    
    filename=r"c:\Users\MMG\Desktop\NBMRS\minor\website\csvfile\recent_activity.csv"
    df2=pd.read_csv(filename)
    
    currentDT = datetime.datetime.now()
    
    for meal_id in l:
        lst=[request.user.username,meal_id,0,0,0,1,currentDT.strftime("%m/%d/%Y %I:%M:%S %p")]
        df2=df2.append(pd.Series(lst,index=df2.columns),ignore_index=True)
        
       
    os.remove(filename)
    df2.to_csv(filename,index=False) 
    
    Profile.objects.filter(number=request.user.username).update(second_time='True')
    
    return redirect('Home')

def order(request):
    if Profile.objects.get(number=request.user.username).second_time:
        filename=r"c:\Users\MMG\Desktop\NBMRS\minor\website\csvfile\recent_activity.csv"
        filename2=r"c:\Users\MMG\Desktop\NBMRS\minor\website\dataset.csv"
                
        df=pd.read_csv(filename)
        df1=pd.read_csv(filename2)
        
        df=df.loc[df["User_Id"]==request.user.username]
        df = df.sort_values(by='Timestamp',ascending=False)
        df=df.drop_duplicates(subset=df.columns.difference(['Timestamp']),keep="last") 
        l=list(df["Meal_Id"])
        data=pd.DataFrame()
        for meal in l:
            df2=df1.loc[df1["Meal_Id"]==meal]
            if data.empty :
                data=df2
            else:
                lst=df2.to_numpy().tolist()
                data=data.append(pd.Series(lst[0],index=df2.columns),ignore_index=True)
                
        data=data.drop_duplicates(subset='Meal_Id', keep="first") 
        
        data=dict(data)
        
        ids=list(data['Meal_Id'])
        n=list(data['Name'])
        c=list(data['catagory'])
        vn=list(data['Veg_Non'])
        r=list(data['Review'])
        nt=list(data['Nutrient'])  
        p=list(data['Price'])   
        sc=c
        
        like=list(df['Liked'])
        rate=list(df['Rated'])
        date=list(df['Timestamp'])
        
        data=zip(n,ids,n,c,sc,vn,r,nt,p,like,rate,date,p)
    
        if request.user.is_authenticated:
            try:
                img= Profile.objects.get(number=request.user.username).image.url
            except:
                img=""
                
            return render(request,'website/orders.html',{'data':data,'image':img})
        
        else:
            return render(request,'website/orders.html')
    else:
        messages.info(request,'you do have not ordered anything')
        return render(request,'website/orders.html')

    
def LikeRate(request):
    if request.method=='POST':
        ids=list(request.POST.get('idsinp').split(','))
        like=list(request.POST.get('likeinp').split(','))
        rate=list(request.POST.get('rateinp').split(','))
        
        filename=r'C:\Users\MMG\Desktop\NBMRS\minor\website\csvfile\recent_activity.csv'
        df=pd.read_csv(filename)
        currentDT = datetime.datetime.now()
        i=0;
        for meal in ids:
            indexNames = df[ (df['User_Id'] ==request.user.username ) & (df['Meal_Id'] == meal) ].index
            df.drop(indexNames , inplace=True)
                
            lst=[request.user.username , meal , rate[i] , like[i] , 0 , 1 , currentDT.strftime("%m/%d/%Y %I:%M:%S %p")]
            df=df.append(pd.Series(lst,index=df.columns),ignore_index=True) #lst = values in list which we want to insert
            os.remove(filename)
            df.to_csv(filename,index=False)
            i=i+1
            
        return redirect('Home')
        