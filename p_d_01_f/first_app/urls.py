from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="homepage"),
    path('form/', views.my_form, name='django_form'),
    
]
