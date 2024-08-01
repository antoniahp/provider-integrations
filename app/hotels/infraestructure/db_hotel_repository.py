from decimal import Decimal
from typing import Sequence

from psycopg2._psycopg import Float

from hotels.domain.hotel_repository import HotelRepository
from hotels.domain.hotel import Hotel


class DbHotelRepository(HotelRepository):
    def get_all_hotels(self) -> Sequence[Hotel]:
        return Hotel.objects.all()

    def filter_hotels_by_name(self, hotel_name: str) -> Sequence[Hotel]:
        return Hotel.objects.filter(hotel_name=hotel_name)

    def filter_hotels_by_rating_gte(self, rating:Float) -> Sequence[Hotel]:
        return Hotel.objects.filter(rating__gte=rating)

    def save_hotel(self, hotel: Hotel) -> None:
        hotel.save()