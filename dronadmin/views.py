from operator import index
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index (request):
    return HttpResponse('Welcome DrOn')
def index (request):
    return render(request,'index.html')