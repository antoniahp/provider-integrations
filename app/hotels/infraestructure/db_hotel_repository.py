from typing import List

from hotels.domain.hotel_repository import HotelRepository
from hotels.domain.hotel import Hotel


class DbHotelRepository(HotelRepository):
    def get_all_hotels(self) -> List[Hotel]:
        return Hotel.objects.all()