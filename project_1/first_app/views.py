from django.shortcuts import render
from django . http import HttpResponse
# Create your views here.
def courses(request):
    return HttpResponse("The courses section")
def about(request):
    return HttpResponse("This is about section")
def home(request):
    return HttpResponse("This is home")