from .models import Profile
from django.shortcuts import render,redirect
from django.contrib import messages

import pandas as pd
import numpy as np
import sklearn
from sklearn.neighbors import NearestNeighbors

df = pd.read_csv(r'C:\Users\MMG\Desktop\NBMRS\minor\website\dataset.csv')

def Recommend(request):
    
    if request.user.is_authenticated:
        class Recommender:
            
            def __init__(self):
                self.df = pd.read_csv(r'C:\Users\MMG\Desktop\NBMRS\minor\website\dataset.csv')
            
            def get_features(self):
                #getting dummies of dataset
                nutrient_dummies = self.df.Nutrient.str.get_dummies()
                disease_dummies = self.df.Disease.str.get_dummies(sep=' ')
                diet_dummies = self.df.Diet.str.get_dummies(sep=' ')
                feature_df = pd.concat([nutrient_dummies,disease_dummies,diet_dummies],axis=1)
             
                return feature_df
            
            def k_neighbor(self,inputs):
                
                feature_df = self.get_features()
               
                #initializing model with k=20 neighbors
                model = NearestNeighbors(n_neighbors=40,algorithm='ball_tree')
                
                # fitting model with dataset features
                model.fit(feature_df)
                
                df_results = pd.DataFrame(columns=list(self.df.columns))
                
                
                # getting distance and indices for k nearest neighbor
                distnaces , indices = model.kneighbors(inputs)
                
                
                for i in list(indices):
                    df_results = df_results.append(self.df.loc[i])
                
                
                df_results = df_results.filter(['Meal_Id','Name','catagory','Nutrient','Veg_Non','Price','Review','Diet','Disease','description'])
                df_results = df_results.drop_duplicates(subset=['Name'])
                df_results = df_results.reset_index(drop=True)
                return df_results
        
        ob = Recommender()
        data = ob.get_features()
        
        total_features = data.columns
        d = dict()
        for i in total_features:
            d[i]= 0
       
        
        p=Profile.objects.get(number=request.user.username) #extract values from database where Table name is Profie
        diet=list(p.diet.split('++'))
        disease=list(p.disease.split('++'))
        nutrient=list(p.nutrient.split('++'))
        
        Recommend_input=diet+disease+nutrient
        
        image=p.image.url
       
        
        for i in Recommend_input: 
            d[i] = 1
        final_input = list(d.values())
        
        results = ob.k_neighbor([final_input]) # pass 2d array []
       
        data=dict(results)
        
        ids=list(data['Meal_Id'])
        n=list(data['Name'])
        c=list(data['catagory'])
        vn=list(data['Veg_Non'])
        r=list(data['Review'])
        nt=list(data['Nutrient'])  
        p=list(data['Price'])
        i=range(len(n))   
        sc=c
        
        data=zip(n,ids,n,c,sc,vn,r,nt,p,p)
        
        return render(request,"website/recommend.html",{'data':data,'image':image})
    
    else:
        messages.error(request,'You must be logged in for meal recommendations..')
        return redirect('Home')
        