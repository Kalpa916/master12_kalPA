from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def input(request):
    return render(request,'base.html')

def add(request):
    x=int(request.GET['t1'])   #getting data from textfields t1 and t2
    y=int(request.GET['t2'])
    z=x+y
    return HttpResponse("<html><body bgcolor='red'><h1>"+str(z)+"</h1></body></html>")

'''
import requests
def home(request):
    response=requests.get("https://api.covid19api.com/countries").json()
    return render(request,'base.html',{'response':response})
'''
