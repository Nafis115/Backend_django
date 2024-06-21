
from django.contrib import admin
from django.urls import path,include
from Task_management_project.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='homepage'),
    path('add_task/',include("taskModel.urls")),
    path('add_category/',include('taskCategory.urls'))
    
]
