from django.urls import path
from taskCategory.views import add_category

urlpatterns = [
   path("add_category/",add_category,name='add_category')
    
]
