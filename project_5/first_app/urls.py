from django.urls import path
from . import views

urlpatterns = [
    path("",views.home ,name='home'),
    path("about/",views.about,name="about"),
    path("forms/", views.forms, name="forms"),
    path("django_forms/",views.StudentData,name="django_forms")
    
]
