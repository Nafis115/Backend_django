from django import forms
from first_app.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        labels={
            'name':'Student name'
        }
        widget={
            'name': forms.TextInput()
        }
        
        help_texts={
            'name': "Enter your full name"
        }
        error_messages ={
            'name':{'required' : "Your name is required"}
        }