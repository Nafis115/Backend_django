from django.shortcuts import render,redirect
from first_app.forms import  GoodsForm
# Create your views here.
def home(request):
    if request.method=='POST':
        form= GoodsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form= GoodsForm()    
    return render(request,'index.html',{'form':form})