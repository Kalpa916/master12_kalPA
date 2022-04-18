from django.db import models

# Create your models here.
class Children(models.Model):
    Children_Name=models.CharField(max_length=120)
    Children_Id=models.IntegerField()
    Children_Father_Name=models.CharField(max_length=56)
    Children_Mother_Namw=models.CharField(max_length=90)
    Children_Roll_No=models.CharField(max_length=90)
    Children_Aadhar_numner=models.IntegerField()
