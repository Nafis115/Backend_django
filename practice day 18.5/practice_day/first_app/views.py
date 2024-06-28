from django.shortcuts import render,redirect
from first_app.forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm,SetPasswordForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def User_Register(request):
    
    if  request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account Create successfully")
            return redirect("signup")
        else:
            messages.warning(request,'Please give valid data')
    else:
        form=RegisterForm()
    return render(request,'register.html',{"form":form})


def User_Login(request):
    if request.method=="POST":
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                messages.success(request,'Log in successfully')
                login(request,user)
                return redirect("profile")
            else:
                messages.warning(request,'Enter valid information')
                return redirect("signup")
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})

@login_required
def profile(request):
    return render(request,'profile.html')
@login_required
def User_Logout(request):
    messages.success(request,"Log out successfully")
    logout(request)
    return redirect("homepage")
@login_required
def UserPassChange(request):
    if request.method=="POST":
        form=SetPasswordForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            messages.success(request,"Password Change successfully")
            update_session_auth_hash(request, user)
            return redirect("profile")
            
        else:
            messages.warning(request,"Give valid password")
    else:
        form=SetPasswordForm(request.user)
    return render(request,'pass_change.html',{'form':form})
@login_required
def UserPassChanged(request):
    if request.method=="POST":
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            messages.success(request,"Password Change successfully")
            update_session_auth_hash(request, user)
            return redirect("profile")
            
        else:
            messages.warning(request,"Give valid password")
    else:
        form=PasswordChangeForm(request.user)
    return render(request,'pass_change.html',{'form':form})
            
            
            
    


            
            