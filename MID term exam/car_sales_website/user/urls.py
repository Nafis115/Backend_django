from django.urls import path
from user.views import UserSignup,UserLogin,UserProfile,UserLogout,UpdateUserProfile,UpdateUserPassword
urlpatterns = [
  path('signup/',UserSignup,name='signup'),
  path('login/',UserLogin.as_view(),name='login'),
  path('profile/',UserProfile,name='profile'),
  path('logout/',UserLogout,name='logout'),
  path("update_profile/", UpdateUserProfile, name="update_profile"),
  path("update_password/", UpdateUserPassword, name="update_password")
]