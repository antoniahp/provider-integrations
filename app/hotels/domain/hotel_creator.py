from decimal import Decimal

from hotels.domain.exceptions.hotel_creator_exception import HotelCreatorException
from hotels.domain.hotel import Hotel


class HotelCreator:
    def create(self, provider_id: str, hotel_name: str, address: str, rating: Decimal, availability: int, price_per_night: Decimal, city: str) -> Hotel:
        if "sexy" in hotel_name:
            raise HotelCreatorException(reason="Bad words")

        return Hotel(
            provider_id=provider_id,
            hotel_name=hotel_name,
            address=address,
            rating=rating,
            availability=availability,
            price_per_night=price_per_night,
            city=city
        )