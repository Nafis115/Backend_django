

from django.urls import path
from first_app.views import User_Register,User_Login,profile,User_Logout,UserPassChange,UserPassChanged


urlpatterns = [

    path('signup/', User_Register,name='signup'),
    path('login/', User_Login,name='login'),
    path('profile/', profile,name='profile'),
    path('logout/', User_Logout,name='logout'),
    path('pass_change/', UserPassChange,name='pass_change'),
    path('pass_changing/', UserPassChanged,name='pass_change_again'),
    
   
]
