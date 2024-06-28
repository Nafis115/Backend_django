from django.urls import path
from first_app.views import home,signup,user_login,profile,user_logout,pass_change
urlpatterns = [
    path("",home,name='homepage'),
    path("signup/",signup,name='signup'),
    path("login/",user_login,name='user_login'),
    path("pass_change/",pass_change,name='passchange'),
    path("profile/",profile,name='profile'),
    path("logout/",user_logout,name='logout')
]
