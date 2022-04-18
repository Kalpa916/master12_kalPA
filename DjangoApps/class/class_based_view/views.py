from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.http import HttpResponse
class Input(View):
    def get(self,request):
        return render(request,'base.html')
class Add(View):
    def post(self,request):
        x=int(request.POST['t1'])
        y=int(request.POST['t2'])
        z=str(x+y)
        return HttpResponse("<html><body bgcolor=red>Sum is :"+z+"</body></html>")
