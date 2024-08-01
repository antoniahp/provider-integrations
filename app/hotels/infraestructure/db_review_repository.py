from uuid import UUID
from typing import Sequence

from hotels.domain.review import Review
from hotels.domain.review_repository import ReviewRepository


class DbReviewRepository(ReviewRepository):

    def filter_by_hotel_id(self, hotel_id: UUID) -> Sequence[Review]:
        return Review.objects.filter(hotel_id=hotel_id)

    def save_review(self, review: Review) -> None:
        review.save()