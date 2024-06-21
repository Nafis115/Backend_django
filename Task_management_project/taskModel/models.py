from django.db import models
from taskCategory.models import Category

# Create your models here.
class Task(models.Model):
    taskTitle=models.CharField(max_length=120) 
    taskDescription=models.TextField() 
    is_completed=models.BooleanField(default=False)
    Task_Assign_Date=models.DateField(null=True,blank=True)
    category=models.ManyToManyField(Category)
    def __str__(self):
        return self.taskTitle
    
