from django.urls import path
from car.views import CarDetailView,PurchaseHistory
urlpatterns = [
  
    path("details/<int:id>", CarDetailView.as_view(), name="car_details"),
    path('purchase/',PurchaseHistory.as_view(),name="purchase")

]
