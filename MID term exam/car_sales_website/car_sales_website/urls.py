from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from car_sales_website.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='homepage'),
    path('brand/<slug:category_slug>/', home, name='brand_wise_car'),
    path('user/', include('user.urls')),
    path("car/",include("car.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
