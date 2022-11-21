from django.contrib import admin

from .models import Student
class adiminview(admin.ModelAdmin):
    list_display = ['name','rollno','address']
# Register your models here.
admin.site.register(Student,adiminview)