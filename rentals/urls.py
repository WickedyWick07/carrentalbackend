# Example in rentals/urls.py
from django.urls import path
from .views import create_rental, get_user_rental

urlpatterns = [
    path('create-rental/', create_rental, name='create_rental'),
    path("rental-details/", get_user_rental, name="get_rentals"),
    # Other paths as needed
]
