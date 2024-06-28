from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   # path('add/',views.add_post,name='add_post'),
   path("add_post/", views.AddPostCreateView.as_view(), name="add_post"),
   path('edit_post/<int:id>',views.UpdatePost.as_view(),name='edit_post'),
   path('delete_post/<int:id>',views.DeletePost.as_view(),name='delete_post'),
   path('details_post/<int:id>',views.DetailsView.as_view(),name='detail_view')
]


