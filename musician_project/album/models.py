from django.db import models
from musician.models import Musician
# Create your models here.
class Rating(models.IntegerChoices):
    ONE = 1, 'One'
    TWO = 2, 'Two'
    THREE = 3, 'Three'
    FOUR = 4, 'Four'
    FIVE = 5, 'Five'

class Album(models.Model):
    AlbumName=models.CharField(max_length=120)
    musician=models.ForeignKey(Musician,on_delete=models.CASCADE)
    AlbumReleaseDate=models.DateField()
    Rating=models.IntegerField(choices=Rating.choices)
    def __str__(self):
        return self.AlbumName