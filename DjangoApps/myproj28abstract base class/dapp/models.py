from django.db import models

# Create your models he
class CommonInfo(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    date=models.DateField()
    class Meta:
        abstract=True

class Student(CommonInfo):
    fees=models.IntegerField()
    date=None


class Teacher(CommonInfo):
    date=models.DateField()
    salary=models.IntegerField()

class Contract(CommonInfo):
    date=models.DateTimeField()
    salary=models.IntegerField()
