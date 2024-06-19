from django.urls import path
from .import views
urlpatterns = [
    path('details/<int:pk>/', views.CarDetails.as_view(), name='car_details'),
    path('create_car/',views.create_car,name='create_car'),
    path('car/buy/<int:pk>/', views.buy_car, name='buy_car'),
]