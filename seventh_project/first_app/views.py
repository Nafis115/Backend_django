from django.shortcuts import render
from . import models,forms
# Create your views here.

def add_student(request):
    form =forms.StudentForm()
    return render(request,"add_student.html",{'form':form})