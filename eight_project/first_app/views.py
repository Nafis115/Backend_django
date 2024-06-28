from django.shortcuts import render,redirect
from first_app.forms import RegistarFrom
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
# Create your views here.
def home(request):
    return render(request,'home.html')
def signup(request):
    if request.method=="POST":
        
        form=RegistarFrom(request.POST)
        
        if form.is_valid():
            messages.success(request,'Account create successfully')
            form.save()
    
    else:
        form=RegistarFrom()
    return render(request,'signup.html',{'form':form})
def user_login(request):
    if request.method=="POST":
        form= AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            name=form.cleaned_data['username']
            user_password=form.cleaned_data['password']
            user=authenticate(username=name,password=user_password) #data ace ki na
            if user is not None:
                login(request,user)
                return redirect('profile')
            
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})

def profile(request):
    if request.user.is_authenticated:
        
        return render(request, 'profile.html', {'user': request.user})
    else:
        return redirect("user_login")

def user_logout(request):
    logout(request)
    return redirect('user_login')

def pass_change(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keep the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(user=request.user)
        
    return render(request, 'passchange.html', {'form': form})
