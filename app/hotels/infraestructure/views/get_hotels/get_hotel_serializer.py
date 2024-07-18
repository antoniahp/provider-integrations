from hotels.domain.hotel import Hotel


class GetHotelSerializer:
    def serialize(self, hotel: Hotel) -> dict:
        return {
            "id": hotel.id,
            "hotel_name": hotel.hotel_name,
            "city": hotel.city,
            "address": hotel.address,
            "rating": hotel.rating,
            "availability":hotel.availability,
            "price_per_night": hotel.price_per_night,
            "amenity": hotel.amenity

        }