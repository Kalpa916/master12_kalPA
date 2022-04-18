from django.shortcuts import render
from .models import Student,Teacher,Contract
# Create your views here.
import datetime
def input(request):
    dt=datetime.datetime.now()
    msg={'date':dt}
    return render(request,'base.html',context=msg)



def view_data(request):
    stu=Student.objects.all()
    teacher=Teacher.objects.all()
    contract=Contract.objects.all()
    return render(request,'base.html',{'stu':stu,'teacher':teacher,'contract':contract})
