from django.shortcuts import render,redirect
from taskModel.forms import TaskFrom
from taskModel.models import Task
# Create your views here.
def add_task(request):
    if request.method=="POST":
        form=TaskFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form=TaskFrom()
    return render(request,'add_task.html',{'form':form})

def edit_task(request,id):
    task=Task.objects.get(pk=id)
    form=TaskFrom(instance=task)
    if request.method=='POST':
        form=TaskFrom(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    return render(request,'add_task.html',{'form':form})

def delete_task(request,id):
    task=Task.objects.get(pk=id)
    task.delete()
    return redirect('homepage')