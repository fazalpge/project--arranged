from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from myapp.serializers import serializerclass
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.models import Employee

def read(request):
    employees = Employee.objects.all()
    return render(request,'test2.html',{'employees': employees})



@api_view(['GET'])
def showemp(request):
  if request.method=='GET':
    results = Employee.objects.all()
    serialize=serializerclass(results,many=True)
    return Response(serialize.data)

def showdata(request):
    callapi = requests.get('http://127.0.0.1:8000/app/show/')
    results = callapi.json()
    return render(request,'test2.html',{'Employees': results})
