from django.db import models

# Create your models here.
class Musician(models.Model):
    FirstName=models.CharField(max_length=120)
    LastName=models.CharField(max_length=120)
    Email=models.EmailField(max_length=120)
    PhoneNumber=models.CharField(max_length=11)
    InstrumentType=models.CharField(max_length=120)
    def __str__(self):
        return self.FirstName