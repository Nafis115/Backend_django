from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from user.forms import RegisterFrom,UserChangeData
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,update_session_auth_hash
from django.views.generic import DetailView,UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
def UserSignup(request):
    if request.method=="POST":
        form=RegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            messages.success(request,'Account create Successfully')
            return redirect('signup')
        else:
            messages.warning(request,'Enter Valid information')
    else:
        form=RegisterFrom()
    return render(request,'register.html',{'form':form})


class UserLogin(LoginView):
    template_name='login.html'
    def get_success_url(self) :
        return reverse_lazy('profile')
    
    
    def form_valid(self, form):
        messages.success(self.request,'Log in successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request,'Enter valid information')
        return super().form_invalid(form)
    
@login_required
def UserLogout(request):
    logout(request)
    return redirect('homepage')
    

@login_required
def UserProfile(request):
    return render(request, 'profile.html', {'id': request.user.id})



@login_required
def UpdateUserProfile(request):
    if request.method=="POST":
        form=UserChangeData(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile update successfully")
            return redirect('profile')
    else:
        form=UserChangeData(instance=request.user)
    return render(request,'update_profile.html',{'form':form})
    
 
@login_required   
def UpdateUserPassword(request):
    if request.method=="POST":
        form=PasswordChangeForm(request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Password update successfully")
            update_session_auth_hash(request,form.user)
            return redirect("profile")
    else:
       
        form=PasswordChangeForm(user=request.user)
    return render(request,'update_profile.html',{'form':form})   
            
            
            
