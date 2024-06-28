from django.shortcuts import render
from car.models import CarModel,CarBrand
def home(request, category_slug=None):
    data=CarModel.objects.all()
    if category_slug is not None:
        brand=CarBrand.objects.get(slug=category_slug)
        data=CarModel.objects.filter(brand=brand)
    brand=CarBrand.objects.all()
    return render(request,'home.html',{'data':data,'brand':brand})

# def home(request):
#     return render(request,'home.html')