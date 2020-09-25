from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.


def index(request):
    return render(request, 'index.html')

def weeklyChart(request):
    return render(request, 'weeklyChart.html')   

def allMarket(request):
    return render(request, 'allMarket.html')

def gussingFrom(request):
    return render(request, 'gussingFrom.html')    


def bharathjodi(request):
    return render(request, 'bharathjodi.html')    

def milanDay(request):
    return render(request, 'milanDay.html')    

def sriDevi(request):
    return render(request, 'sriDevi.html')

def timeBazar(request):
    return render(request, 'timeBazar.html')   

def paneltime(request):
    return render(request, 'paneltime.html')

def panelBharath(request):
    return render(request, 'panelBharath.html')

def panelmilan(request):
    return render(request, 'panelmilan.html')


def panelseridevi(request):
    return render(request, 'panelseridevi.html')


# def handleSignup(request):
#     if request.method =='POST':
#         UserName = request.POST['UserName']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         email = request.POST['email']


#         if len(UserName)>10:
#             messages.ERROR(request,'not valid name')
#             return redirect('signup.html')  

#         if password1 != password2:
#             messages.ERROR(request,'not valid password')
#             return redirect('signup.html') 
             

#         myuser = User.objects.create_user(username=UserName,password=password1,email=email)
#         myuser.save() 
#         messages.success(request,"you are sucessfly loged in")
  
    
#     return render(request,'signup.html')
    
   

    

     

        



    
    
    


