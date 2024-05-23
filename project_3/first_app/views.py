from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    d={'author': 'Nafis', 'list':['python','is','best'],'birthday':datetime.datetime.now(),
       'empty':'','age': 30, 'course':[
        {
       "id":1,
       'name':'python',
       'fee': 500,
        },
        {
       "id":2,
       'name':'java',
       'fee': 400,
        },
        {
       "id":3,
       'name':'English',
       'fee': 5000,
        },
        {
       "id":4,
       'name':'Math',
       'fee': 6000,
        },
        ]}
    return  render (request,"home.html", d)