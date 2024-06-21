from django.shortcuts import render

def home(request):
  from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    context = {
        'author': 'rahim',
        'age': 5,
        'lst': ['python', 'is', 'best'],
        'birthday': datetime.datetime.now(),
        'val':  '',
        'add':10,
        'courses': [
            {'id': 1, 'name': 'Python', 'fee': 5000},
            {'id': 2, 'name': 'Django', 'fee': 10000},
            {'id': 3, 'name': 'C', 'fee': 1000}
        ]
    }
    return render(request,"first_app/index.html",context)