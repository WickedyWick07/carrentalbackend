from django.db import models
from django.contrib.auth.models import User
from cars.models import Car

# Create your models here.
class Rental(models.Model):
    id = models.AutoField(primary_key=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rental_date = models.DateField()
    pickup_time = models.TimeField(null=True)
    return_time = models.TimeField(null=True)
    return_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} rented {self.car}"


