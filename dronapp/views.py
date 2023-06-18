from operator import index
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index (request):
    return HttpResponse('Welcome DrOn')

def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def book(request):
    return render(request,'book.html')
def covid_consultation(request):
    return render(request,'covid_consultation.html')
def dermatology(request):
    return render(request,'dermatology.html')
def ent(request):
    return render(request,'ent.html')
def gynecology(request):
    return render(request,'gynecology.html')
def pediatrics(request):
    return render(request,'pediatrics.html')
def physician(request):
    return render(request,'physician.html')
def myprofile(request):
    return render(request,'myprofile.html')

    
    