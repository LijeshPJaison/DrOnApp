from unicodedata import name
from django import views
from django.urls import path
from.import views
urlpatterns = [
    path('index',views.index),
    path('doctorhome',views.doctorhome, name='doctorhome'),
    path('doctorlogin',views.doctorlogin, name='doctorlogin'),
    path('doctorsignup',views.doctorsignup, name='doctorsignup'),
    path('myprofile',views.myprofile, name='myprofile'),
    path('doctortimeset',views.doctortimeset, name='doctortimeset')
]