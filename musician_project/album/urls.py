from django.urls import path
from album.views import add_album,edit_album,delete_album

urlpatterns = [
   
    path('add_album/',add_album,name='add_album'),
    path('edit_album/<int:id>',edit_album,name='edit_album'),
    path('delete_album/<int:id>',delete_album,name='delete_album'),
    
]