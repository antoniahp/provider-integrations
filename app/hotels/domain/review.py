from uuid import uuid4
from django.db import models

from hotels.domain.hotel import Hotel


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="reviews")
    user_name = models.CharField(max_length=120)
    review = models.DecimalField(max_digits=3, decimal_places=2)
    title = models.CharField(max_length=120)
    text = models.TextField()
    published_at = models.DateField()

    def __str__(self):
        return self.title