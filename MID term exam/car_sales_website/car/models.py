from django.db import models
from django.utils.text import slugify

class CarBrand(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(CarBrand, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    

class CarModel(models.Model):
    name=models.CharField(max_length=120)
    price=models.CharField(max_length=120)
    image=models.ImageField(upload_to='car/media/uploads')
    descriptions=models.TextField()
    quantity=models.PositiveIntegerField(default=0)
    brand=models.ForeignKey(CarBrand,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
    
