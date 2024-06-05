from . import views
from django.urls import include, path

urlpatterns = [
    path('read/', views.read),
    #path('display/', views.display),
    path('show/', views.showemp,name='showemp'),
    path('data/', views.showdata,name='showdata'),
]
