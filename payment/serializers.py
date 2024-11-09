# serializers.py
from rest_framework import serializers
from .models import PaymentForm, Rental

class PaymentSerializer(serializers.ModelSerializer):
    rental_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = PaymentForm
        fields = '__all__'

    