from abc import ABC, abstractmethod
from typing import Sequence

from hotels.domain.hotel import Hotel

class HotelRepository(ABC):
    @abstractmethod
    def get_all_hotels(self) -> Sequence[Hotel]:
        pass

    @abstractmethod
    def filter_hotels_by_name(self, hotel_name:str) -> Sequence[Hotel]:
        pass

    @abstractmethod
    def filter_hotels_by_rating_gte(self, rating_gte:float) -> Sequence[Hotel]:
        pass

    @abstractmethod
    def save_hotel(self , hotel: Hotel) -> None:
        pass
