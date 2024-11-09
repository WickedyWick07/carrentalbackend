from django.db import models
from django.contrib.auth.models import User
from rentals.models import Rental
from datetime import date

# Create your models here.
class PaymentForm(models.Model):

    CARD_TYPE_CHOICES = [
        ('debit', 'Debit'),
        ('credit', 'Credit'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE, null=True)
    card_type = models.CharField(max_length=10, choices=CARD_TYPE_CHOICES, null=True)
    card_number = models.BigIntegerField(null=True)
    cvv = models.IntegerField( null=True)
    expiry_date = models.DateField()

    def __str__(self):
        # Ensure we handle cases where card_number might be None
        card_number_str = str(self.card_number) if self.card_number else "N/A"
        return f"{self.user} - {self.card_type} - {card_number_str[-4:]}"

    def formatted_expriy_date(self):
        return self.expiry_date.strftime("%m/%Y")