from . import views
from django.urls import include, path

urlpatterns = [
    path('read/', views.read),
    #path('display/', views.display),
   
]
