
from django.contrib import admin
from django.urls import path,include
from practice_day.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name='homepage'),
    path('first/', include("first_app.urls"))
]
