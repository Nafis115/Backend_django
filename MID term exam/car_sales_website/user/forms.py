from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from user.models import Comment

class RegisterFrom(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['name','email','body']
        
        
class UserChangeData(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        

