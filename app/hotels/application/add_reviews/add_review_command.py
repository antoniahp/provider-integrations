from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from uuid import UUID
from cqrs.commands.command import Command


@dataclass(frozen=True)
class AddReviewCommand(Command):
    review_uuid: UUID
    hotel_name: str
    user_name: str
    review: Decimal
    title: str
    text: str
    published_at: date
