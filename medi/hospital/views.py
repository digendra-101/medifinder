



from datetime import date
from email.mime import image
from tkinter import Image
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import hos_list , reviews

# Create your views here.

def home(request):
    auth_logout(request)
    return render(request,'index.html')




fn=""
email =""
password =""

def login(request):

    if request.method == 'POST':
        em = request.POST.get("username")
        pas = request.POST.get("password")
        
        user = authenticate(request,username=em,password=pas)
        if user is not None :
            auth_login(request,user)
            return redirect('welcome')
        else :
            return HttpResponse("wrong password")    


    

    return render(request,'login.html')

def logout(request):
    auth_logout(request)
    return redirect('home')  

def signup(request):
   
    if request.method =='POST':
        fn = request.POST.get('first_name')
        
        email = request.POST.get('email')
        password = request.POST.get('password')

        my_user =User.objects.create_user(fn,email,password)
        my_user.save()
        return redirect('login') 




    return render(request,'signup.html')

@login_required(login_url='login')
def welcome(request):

    return render(request,'welcome.html')


def search(request):
    
    
    hos_lists = hos_list.objects.all()    
    
    print(hos_lists) 
    n= len(hos_lists)
    params ={'no of slides':n , 'range':range(n) , 'hos_lists':hos_lists}


    return render(request,'search.html', params)


@login_required(login_url='login')
def register_hos(request):
    
    if request.method=='POST':
       
        hospitalname= request.POST.get('hospital_name')
        discr= request.POST.get('discription')
        date1= request.POST.get('date')
        location1= request.POST.get('location')
        image1 = request.POST.get('img')
        services1 = request.POST.get('services')
        contact1 = request.POST.get('contact')
        hos_beds1 = request.POST.get('hos_beds')

        em = hos_list(hos_name=hospitalname,desc=discr,date=date1,location=location1,image=image1,services=services1,contact=contact1,hos_beds = hos_beds1)
        em.save()
        print(em)
        
        

    return render(request,'register_hos.html')


def hos_profile(request,id):
    
    hoslist = hos_list.objects.filter(id=id)
    if request.method == "POST":
        reviews1 = request.POST.get("reviews")

        re = reviews(reviewm=reviews1)
        re.save()
    
    rev = reviews.objects.all()
    return render(request,"hos_profile.html",{"hoslist":hoslist[0],"rev":rev[:]})


def query(request):
    query1=request.GET.get('query')
    hos_lists = hos_list.objects.filter(hos_name__icontains=query1)   
    
    print(hos_lists) 
    n= len(hos_lists)
    params ={'hos_lists':hos_lists}


    return render(request,'query.html', params)  


