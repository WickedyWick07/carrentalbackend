from django.db import models

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)   
    year = models.IntegerField()
    availability = models.BooleanField(default=True)
    image = models.ImageField( upload_to='cars/images', null=True, blank=True)

    def __str__(self):
        return f"{self.make} {self.model} {self.year}"
    