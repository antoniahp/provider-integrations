from django.contrib import admin
from hotels.domain.amenity import Amenity
from hotels.domain.hotel import Hotel

# Register your models here.
admin.site.register(Hotel)
admin.site.register(Amenity)