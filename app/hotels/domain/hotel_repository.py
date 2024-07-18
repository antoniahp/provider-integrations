from abc import ABC
from typing import List

from hotels.domain.hotel import Hotel


class HotelRepository(ABC):
    def get_all_hotels(self) -> List[Hotel]:
        pass