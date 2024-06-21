from django.shortcuts import render,redirect
from taskCategory.forms import categoryForm
# Create your views here.
def add_category(request):
    if request.method=="POST":
        form=categoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_category')
    else:
        form=categoryForm()
    return render(request,'add_category.html',{'form':form})