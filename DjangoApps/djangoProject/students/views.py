from django.shortcuts import render

# Create your views here.
def input(request):
    sname="kalpataru sahoo"
    rollno=121
    sal=50000
    dept=20
    dict1={'sname':sname,'roll':rollno,'sal':sal,'dept':dept}
    return render(request,'base.html',context=dict1)