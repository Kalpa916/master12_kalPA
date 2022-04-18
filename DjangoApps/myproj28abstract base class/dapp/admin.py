from django.contrib import admin
from .models import Student,Teacher,Contract
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','age','fees']
admin.site.register(Student,StudentAdmin)
class TeacherAdmin(admin.ModelAdmin):
    list_display=['id','name','age','date','salary']
admin.site.register(Teacher,TeacherAdmin)
class ContractAdmin(admin.ModelAdmin):
    list_display=['id','name','age','date','salary']
admin.site.register(Contract,ContractAdmin)
