from unicodedata import name
from django import views
from django.urls import path
from.import views
urlpatterns = [
    path('index',views.index),
    path('home',views.home, name='home'),
    path('login',views.login, name='login'),
    path('signup',views.signup, name='signup'),
    path('book',views.book, name='book'),
    path('covid_consultation',views.covid_consultation, name='covid_consultation'),
    path('dermatology',views.dermatology, name='dermatology'),
    path('ent',views.ent, name='ent'),
    path('gynecology',views.gynecology, name='gynecology'),
    path('pediatrics',views.pediatrics, name='pediatrics'),
    path('physician',views.physician, name='physician'),
    path('myprofile',views.myprofile, name='myprofile')
]
