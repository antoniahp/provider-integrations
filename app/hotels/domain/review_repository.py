from abc import ABC, abstractmethod
from typing import Sequence

from hotels.domain.review import Review


class ReviewRepository(ABC):
    @abstractmethod
    def filter_by_hotel_id(self,hotel_id: str) -> Sequence[Review]:
        pass

    @abstractmethod
    def save_review(self, review: Review) -> None:
        pass