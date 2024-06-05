from django.shortcuts import render
from myapi.models import Attritiondata
from myapi.forms import attritionForm
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
import requests
import pickle
import joblib
from sklearn import preprocessing 
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from myapi.serializers import serializerclass
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from sklearn.preprocessing import LabelEncoder
import os

#load_model_path = './mlmodel/attr_pipe.pkl'

# if os.path.exists(load_model_path):
#     model = joblib.load(load_model_path)
#     # print(model)
#     print('Model Found')
# else:
#     print("Pathe not Found")




# Create your views here.
class attritionView(viewsets.ModelViewSet):
    queryset= Attritiondata.objects.all()
    serializers_class= serializerclass
    
    # def load_model():
    #     load_model_path = '/erptools/myapi/mlmodel/attr_pipe.pkl'
    #     return load_model_path
#/Users/DELL/projectformit/mlmodel/attr_pipe.pkl   
# C:\Users\DELL\projectformit\erptools\mlmodel   

# def prediction(df):
#   load_model_path = './mlmodel/attr_pipe.pkl'
# #   mdl=joblib.load(load_model_path)
# #   y_pred = mdl.predict(df)
#   model = joblib.load(load_model_path)

#   expected_dtype = np.dtype({'names': ['left_child', 'right_child', 'feature', 'threshold', 'impurity', 'n_node_samples', 'weighted_n_node_samples', 'missing_go_to_left'],
#                                'formats': ['<i8', '<i8', '<i8', '<f8', '<f8', '<i8', '<f8', 'u1'],
#                                'offsets': [0, 8, 16, 24, 32, 40, 48, 56],
#                                'itemsize': 64})

#   if isinstance(model, np.ndarray) and model.dtype != expected_dtype:
#         model = model.astype(expected_dtype)   
#   print(model)
         
  
# #   print(mdl)
    
#   return model
    
def load_model(df):
    load_model_path = './mlmodel/attr_pipe.pkl'
    model = joblib.load(load_model_path)
    return model
        
# Check and convert dtype if needed


# def prediction(df):
# #    mdl=joblib.load("./mlmodel/attr_pipe.pkl")
#    mdl =  joblib.load('./')
#    print(mdl)
   #attr_pipe= joblib.load("C:/Users/DELL/projectformit/mlmodel/attr_pipe.pkl")
   #y_pred = attr_pipe.predict(df)

    # load_model_path = '/erptools/myapi/mlmodel/attr_pipe.pkl'
    # model = joblib.load(load_model_path)
    # print(model)
# model = joblib.load('../myapi/mlmodel/attr_pipe.pkl')
# print(model)

#    return mdl
    

# def show(request):
#     if request.method == "POST":
#         form = attritionForm(request.POST)
#         if form.is_valid():
#             myDict = form.cleaned_data
#             df = pd.DataFrame(myDict,index=[0])
#             model = load_model()
#             result = prediction(model,df)
#             print(result)
#     form= attritionForm()

#     return render(request, "test.html", {"form": form })
        
      
def show(request):
    if request.method == "POST":
        form = attritionForm(request.POST)
        if form.is_valid():
            Age = form.cleaned_data['Age']
            BusinessTravel= form.cleaned_data['BusinessTravel']
            DailyRate= form.cleaned_data['DailyRate']
            Department= form.cleaned_data['Department']
            DistanceFromHome= form.cleaned_data['DistanceFromHome']
            Education= form.cleaned_data['Education']
            EducationField= form.cleaned_data['EducationField']
            EmployeeNumber=form.cleaned_data['EmployeeNumber']
            EnvironmentSatisfaction=form.cleaned_data['EnvironmentSatisfaction']
            Gender= form.cleaned_data['Gender']
            HourlyRate= form.cleaned_data['HourlyRate']
            JobInvolvement= form.cleaned_data['JobInvolvement']
            JobLevel=form.cleaned_data['JobLevel']
            JobRole= form.cleaned_data['JobRole']
            JobSatisfaction=form.cleaned_data['JobSatisfaction']
            MaritalStatus= form.cleaned_data['MaritalStatus']
            MonthlyIncome= form.cleaned_data['MonthlyIncome']
            MonthlyRate= form.cleaned_data['MonthlyRate']
            NumCompaniesWorked= form.cleaned_data['NumCompaniesWorked']
            OverTime= form.cleaned_data['OverTime']
            PercentSalaryHike= form.cleaned_data['PercentSalaryHike']
            PerformanceRating= form.cleaned_data['PerformanceRating']
            RelationshipSatisfaction=form.cleaned_data['RelationshipSatisfaction']
            StockOptionLevel=form.cleaned_data['StockOptionLevel']
            TotalWorkingYears= form.cleaned_data['TotalWorkingYears']
            TrainingTimesLastYear= form.cleaned_data['TrainingTimesLastYear']
            WorkLifeBalance= form.cleaned_data['WorkLifeBalance']
            YearsAtCompany= form.cleaned_data['YearsAtCompany']
            YearsInCurrentRole= form.cleaned_data['YearsInCurrentRole']
            YearsSinceLastPromotion= form.cleaned_data['YearsSinceLastPromotion']
            YearsWithCurrManager= form.cleaned_data['YearsWithCurrManager']
            myDict = (request.POST).dict()
            df = pd.DataFrame(myDict,index=[0])
            print(load_model(df))
                          
    form= attritionForm()
    return render(request, "test.html", {"form": form })



# def show(request):
#     if request.method == "POST":
#         try:
#             post_data = json.loads(request.body.decode('utf-8'))
#             df = pd.DataFrame([post_data])
#             model = load_model()
#             result = prediction(model,df)
#             return JsonResponse({'result':result})
#         except json.JSONDecodeError as e:
#             return JsonResponse({'error':'Invalid Json format'},status=400)
        
#     return JsonResponse({'error':'Invalid Json format2'},status=400)
    

