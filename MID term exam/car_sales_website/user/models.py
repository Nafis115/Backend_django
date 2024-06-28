from django.db import models
from car.models import CarModel
from django.contrib.auth.models import User
# Create your models here.
class Comment(models.Model):
    
    car=models.ForeignKey(CarModel,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=120)
    email=models.EmailField()
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"comment by {self.name}"
    
class Purchase(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    car=models.ForeignKey(CarModel,on_delete=models.CASCADE,null=True,blank=True)
    purchase_date=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'{self.user.username} - {self.car.name}'
    