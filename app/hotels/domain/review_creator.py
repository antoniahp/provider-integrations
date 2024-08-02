from datetime import date
from decimal import Decimal
from uuid import UUID
from hotels.domain.review import Review

class ReviewCreator:
    def create(self, review_uuid:UUID, hotel_id: UUID, user_name: str, review: Decimal, title: str, text: str, published_at: date):
        #Validaciones universales
        return Review(
            review_uuid=review_uuid,
            hotel_id=hotel_id,
            user_name=user_name,
            review=review,
            title=title,
            text=text,
            published_at=published_at
        )
