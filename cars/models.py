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
    #add direct image url function
    #https://carrentalbackend-0zuw.onrender.com/media/https%3A/xecpdpctpkqjzukczgoe.supabase.co/storage/v1/object/public/car-images/2023-Lexus-RX_KL_10.webp fix this url
    # run from local server to test the functionality of the images
    @property
    def full_image_url(self):
        if self.image:
            # Get the file path without any prepended base URL
            file_path = self.image.name.replace('cars/images/', '')  # Remove any unwanted prefix
            return f"https://xecpdpctpkqjzukczgoe.supabase.co/storage/v1/object/public/car-images/{file_path}"
        return None