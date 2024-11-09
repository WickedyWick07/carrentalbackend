from django.urls import path
from .views import payment_form, RentalDetailView

urlpatterns = [
    # Define URL pattern for PaymentFormView
    path('payment/<int:rental_id>/', payment_form, name='payment-form'),

    # Define URL pattern for RentalDetailView
    path('rentals/<int:rental_id>/', RentalDetailView.as_view(), name='rental-detail'),
]
