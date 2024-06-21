from django.shortcuts import render
from . forms import contactForm,StudentForm

def home(request):
    return render(request,"./first_app/home.html")

def about(request):
    if request.method=='POST':
        name=request.POST.get("Name")
        email=request.POST.get("Email")
        select=request.POST.get("select")
        return render(request,"./first_app/about.html",{'name':name,'email':email,'select':select})
    else:
        return render(request,"./first_app/about.html")
    
  

def forms(request):
    
    if request.method=='POST':
        name=request.POST.get("Name")
        email=request.POST.get("Email")
        select=request.POST.get("select")
        return render(request,"./first_app/forms.html",{'name':name,'email':email,'select':select})
    else:
        return render(request,"./first_app/forms.html")
   

def DjangoForm(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./first_app/upload/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
    else:
        form = contactForm()
    return render(request, './first_app/django_forms.html', {'form':form}) 

def StudentData(request):
    if request.method=="POST":
        form=StudentForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
            form=StudentForm()
    return render(request, './first_app/django_forms.html', {'form':form})