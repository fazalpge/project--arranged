from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from myapp.serializers import serializerclass
from rest_framework.response import Response

from testing.models import Employee

# Create your views here.
def read(request):
    employees = Employee.objects.all()
    data = serializers.serialize('json', employees)
    return JsonResponse(data, safe=False)





