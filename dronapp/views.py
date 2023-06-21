from operator import index
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import*
from .decorators import auth_user
from django.http import JsonResponse

# Create your views here.
@auth_user
def indexFunction(request):
    return render(request,'index.html')

@auth_user
def homeFunction(request):
    return render(request,'home.html')

def loginFunction(request):
    message = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        check_user = Signup.objects.filter(username=username, password=password)
        if check_user:
            request.session['signup'] = username
            return redirect('home')
        else:
            message = "Please Enter Valid Username"
    return render(request, 'login.html',{'message':message})

def signupFunction(request):
    message=""
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        mobile_number = request.POST['mobile_number']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        sign = Signup(name=name,username=username,email=email,mobile_number=mobile_number,password=password,confirm_password=confirm_password)
        query = Signup.objects.filter(username=username)
        if not query :
            sign.save()
            return redirect('login')
        else:
            message = 'username already exist'      
    return render(request,'signup.html',{'message':message})

@auth_user
def LogoutFunction(request):
    try:
        del request.session['signup']
    except:
        return redirect('login')
    return redirect('login')

@auth_user
def bookingFunction(request):
    if request.method == 'POST':
        name = request.POST['name']
        mobile_number = request.POST['mobile_number']
        select_hospital = request.POST['select_hospital']
        select_department = request.POST['select_department']
        select_doctor = request.POST['select_doctor']
        date = request.POST['date']
        time = request.POST['time']
        booking = Booking(name=name, mobile_number=mobile_number, select_hospital = select_hospital, select_department = select_department, select_doctor = select_doctor, date = date, time = time)
        booking.save()
    return render(request,'booking.html')

@auth_user
def covidConsultationFunction(request):
    return render(request,'covid_consultation.html')

@auth_user
def dermatologyFunction(request):
    return render(request,'dermatology.html')

@auth_user
def entFunction(request):
    return render(request,'ent.html')

@auth_user
def gynecologyFunction(request):
    return render(request,'gynecology.html')

@auth_user
def pediatricsFunction(request):
    return render(request,'pediatrics.html')

@auth_user
def physicianFunction(request):
    return render(request,'physician.html')

@auth_user
def myprofileFunction(request):
    return render(request,'myprofile.html')