from abc import ABC, abstractmethod
from typing import List
from hotels.domain.hotel import Hotel

class HotelRepository(ABC):
    @abstractmethod
    def get_all_hotels(self) -> List[Hotel]:
        pass