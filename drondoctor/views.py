from operator import index
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index (request):
    return HttpResponse('Welcome DrOn')


def doctorhome(request):
    return render(request,'doctorhome.html')
def doctorlogin(request):
    return render(request,'doctorlogin.html')
def doctorsignup(request):
    return render(request,'doctorsignup.html')
def myprofile(request):
    return render(request,'myprofile.html')
def doctortimeset(request):
    return render(request,'doctortimeset.html')