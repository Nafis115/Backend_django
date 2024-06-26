from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path("signup/",views.register,name='register'),
   path('login/',views.user_login,name='login'),
   path('logout/',views.user_logout,name='logout'),
   path("profile/", views.profile, name="profile"),
   path("profile/edit", views.edit_profile, name="edit_profile"),
   path("profile/pass_change/",views.pass_change,name='pass_change')
]
