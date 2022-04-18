'''

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def input(request):
    return render(request,'base.html')
def compute(request):
    x=int(request.GET['t1'])
    y=int(request.GET['t2'])
    z=int(request.GET['t3'])
    k=x+y+z
    return HttpResponse("<html><body>"+str(k)+"</body></html>")
'''
from django.shortcuts import render
from django.http import HttpResponse
from . models import Children

def input(request):
    return render(request,'base.html')
def compute(request):
    Children_Name=request.GET['t1']
    Children_Id=request.GET['t2']
    Children_Father_Name=request.GET['t3']
    Children_Mother_Namw=request.GET['t4']
    Children_Roll_No=request.GET['t5']
    Children_Aadhar_numner=request.GET['t6']
    p=Children(Children_Name=Children_Name,Children_Id=Children_Id,Children_Father_Name=Children_Father_Name,Children_Mother_Namw=Children_Mother_Namw,Children_Roll_No=Children_Roll_No,Children_Aadhar_numner=Children_Aadhar_numner)
    p.save()
    return HttpResponse('Data inserted succesfully')
def retrieve(request):
    pass
