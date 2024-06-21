from django.urls import path
from taskModel.views import add_task,edit_task,delete_task

urlpatterns = [
   path('add_task/',add_task,name='add_task'),
   path('edit_task/<int:id>',edit_task,name='edit_task'),
   path('delete_task/<int:id>',delete_task,name='delete_task')
    
]
