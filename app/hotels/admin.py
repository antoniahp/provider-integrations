from django.contrib import admin
from hotels.domain.amenity import Amenity
from hotels.domain.hotel import Hotel
from hotels.domain.review import Review

# Register your models here.
admin.site.register(Hotel)
admin.site.register(Amenity)
admin.site.register(Review)