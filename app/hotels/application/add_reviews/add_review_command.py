from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from cqrs.commands.command import Command


@dataclass(frozen=True)
class AddReviewCommand(Command):
    hotel_name: str
    user_name: str
    review: Decimal
    title: str
    text: str
    published_at: date
