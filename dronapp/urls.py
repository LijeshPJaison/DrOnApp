from unicodedata import name
from django import views
from django.urls import path
from.import views

urlpatterns = [
    path('index',views.indexFunction, name='index'),
    path('home',views.homeFunction, name='home'),
    path('login',views.loginFunction, name='login'),
    path('signup',views.signupFunction, name='signup'),
    path('logout',views.LogoutFunction, name='logout'),
    path('booking',views.bookingFunction, name='booking'),
    path('covid_consultation',views.covidConsultationFunction, name='covid_consultation'),
    path('dermatology',views.dermatologyFunction, name='dermatology'),
    path('ent',views.entFunction, name='ent'),
    path('gynecology',views.gynecologyFunction, name='gynecology'),
    path('pediatrics',views.pediatricsFunction, name='pediatrics'),
    path('physician',views.physicianFunction, name='physician'),
    path('myprofile',views.myprofileFunction, name='myprofile'),
]
