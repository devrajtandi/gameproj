from django.shortcuts import render
from django.shortcuts import HttpResponse

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
 


