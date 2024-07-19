from django.urls import path
from hotels.infraestructure.views.get_hotels.get_hotel_view import GetHotelView

urlpatterns = [
    path("",GetHotelView.as_view(), name="hotel")

]