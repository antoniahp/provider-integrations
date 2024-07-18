from django.db import models
from uuid import uuid4
from hotels.domain.amenity import Amenity


class Hotel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    provider_id = models.CharField(max_length=120)
    hotel_name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    rating = models.DecimalField(max_digits=10, decimal_places=10)
    availability = models.IntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=10)
    city = models.CharField(max_length=120)
    amenity = models.ManyToManyField(Amenity)

    def __str__(self):
        return self.hotel_name