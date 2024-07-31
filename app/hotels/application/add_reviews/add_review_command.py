from dataclasses import dataclass
from datetime import date
from unicodedata import decimal
from uuid import UUID

from cqrs.commands.command import Command


@dataclass(frozen=True)
class AddReviewCommand(Command):
    hotel_name: str
    user_name: str
    review: decimal
    title: str
    text: str
    published_at: date
