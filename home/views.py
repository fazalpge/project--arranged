from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
# Create your views here.
from django.http import HttpResponse

class employeeApiview(APIView):
     def get(self,request):
        #  allemployee = employee.objects.all().values()
         return Response({"message":"employee attrition","result":'allemployee'})
     
     #def post(self,request):
        # employee.objects.create(id =request.data["id"],
                                # employee_at_risk=request.data["atrisk"],
                                # employee_not_at_risk=request.data["notrisk"]
                                # )
        # employee = employee.objects.all().filter(id =request.data["id"]).values()
       #  return Response({"message":"employee attrition data","result is":employee}) 

def test (request):
    return render(request,'test.html')

def dashboard (request):
    return render(request,'dashboard.html')