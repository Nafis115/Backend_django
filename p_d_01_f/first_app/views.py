from django.shortcuts import render
from .forms import MyForm

def home(request):
    return render(request, './first_app/home.html')

def my_form(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
           
            return render(request, './first_app/django_form.html', {'form': form, 'data': form.cleaned_data})
    else:
        form = MyForm()

    return render(request, './first_app/django_form.html', {'form': form})