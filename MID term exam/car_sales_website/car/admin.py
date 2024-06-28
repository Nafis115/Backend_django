from django.contrib import admin
from car.models import CarModel,CarBrand
# Register your models here.
admin.site.register(CarModel)
admin.site.register(CarBrand)