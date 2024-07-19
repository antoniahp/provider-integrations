from typing import List

from hotels.domain.amenity import Amenity
from hotels.domain.hotel import Hotel


class GetHotelSerializer:
    def serialize_amenities(self, amenities: List[Amenity])->List[dict]:
        amenities_list = []
        for amenity in amenities:
            amenities_list.append({
                "id": amenity.id,
                "name": amenity.name
            })
        return amenities_list

    def serialize(self, hotels: List[Hotel]) -> List[dict] :
        hotel_list = []
        for hotel in hotels:
            serialize_amenities = self.serialize_amenities(amenities = hotel.amenity.all())
            hotel_list.append({
                "id": hotel.id,
                "hotel_name": hotel.hotel_name,
                "city": hotel.city,
                "address": hotel.address,
                "rating": hotel.rating,
                "availability":hotel.availability,
                "price_per_night": hotel.price_per_night,
                "amenity": serialize_amenities
            })

        return hotel_list
