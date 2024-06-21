
from django.urls import path
from musician.views import add_musician,edit_musician

urlpatterns = [
   
    path('add_musician/',add_musician,name='add_musician'),
    path('edit_musician/<int:id>',edit_musician,name='edit_musician'),
    
]