from django import forms
from django.core import validators

class contactForm(forms.Form):
    name=forms.CharField(label="Username")
    email=forms.EmailField(label="Useremail")
    age=forms.CharField(widget=forms.NumberInput)
    weight=forms.FloatField()
    balance=forms.DecimalField()
    age=forms.CharField()
    check=forms.BooleanField()
    appointment = forms.CharField(widget=forms.DateInput(attrs= {'type' : 'datetime-local'}))
    brithday=forms.DateField(widget=forms.DateInput)
    CHOICES=[('s','small'),('m','medium'),('l', 'large')]
    size=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
    MEAL = [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    pizza=forms.MultipleChoiceField(choices=MEAL,widget=forms.CheckboxSelectMultiple)
    file=forms.FileField()
   
   
class StudentForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput)
    email=forms.CharField(widget=forms.EmailInput)
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data=super().clean()
        valuename=self.cleaned_data['name']
        valueemail=self.cleaned_data['email']
        valpass=self.cleaned_data['password']
        c_valpass=self.cleaned_data['confirm_password']
        
        
        if len(valuename)<10:
            raise forms.ValidationError(message="name cannot less than 10")
        if ".com" not in valueemail:
            raise forms.ValidationError(message="Your email must contain .com")
        if valpass != c_valpass:
            raise forms.ValidationError(message="passoword didn't match")
