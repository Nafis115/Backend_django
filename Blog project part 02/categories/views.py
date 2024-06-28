from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_categories(request):
    if request.method=="POST":
        categoryForm=forms.CategoryForm(request.POST)
        if categoryForm.is_valid():
            categoryForm.save()
            return redirect("add_category")
    else:
        categoryForm=forms.CategoryForm()
    return render(request,"add_category.html",{'form':categoryForm})