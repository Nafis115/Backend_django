from django.db import models

class Student(models.Model):
    name =(models.CharField(max_length=20))
    roll =(models.IntegerField(primary_key=True))
    address=models.TextField()
    
def __str__(self):
    return self.name

