from django import forms
from taskModel.models import Task
class TaskFrom(forms.ModelForm):
    class Meta:
        model=Task
        fields='__all__'
        widgets = {
            'Task_Assign_Date': forms.DateInput(attrs={'type': 'date'}),
        }