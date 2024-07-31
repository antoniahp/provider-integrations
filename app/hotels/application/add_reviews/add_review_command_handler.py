from typing import Sequence

from django.db import transaction

from cqrs.commands.command_handler import CommandHandler
from hotels.application.add_reviews.add_review_command import AddReviewCommand
from hotels.domain.exceptions.hotel_by_name_not_found_exception import HotelByNameNotFoundException
from hotels.domain.hotel_repository import HotelRepository
from hotels.domain.review import Review
from hotels.domain.review_creator import ReviewCreator
from hotels.domain.review_repository import ReviewRepository


class AddReviewCommandHandler(CommandHandler):
    def __init__(self, review_repository: ReviewRepository, review_creator: ReviewCreator, hotel_repository: HotelRepository):
        self.review_repository = review_repository
        self.review_creator = review_creator
        self.hotel_repository = hotel_repository

    def handle(self, command: AddReviewCommand):
        filtered_hotels_by_name = self.hotel_repository.filter_hotels_by_name(hotel_name=command.hotel_name)
        if len(filtered_hotels_by_name) == 0:
            raise HotelByNameNotFoundException(hotel_name=command.hotel_name)
        for hotel in filtered_hotels_by_name:
            hotel_review = self.review_creator.create(
                hotel_id=hotel.id,
                user_name=command.user_name,
                review=command.review,
                title=command.title,
                text=command.text,
                published_at=command.published_at
            )

            self.review_repository.save_review(review=hotel_review)

            hotel_reviews = self.review_repository.filter_by_hotel_id(hotel_id=hotel.id)
            hotel.rating = self.__calculate_means_of_opinions(hotel_reviews=hotel_reviews)

            self.hotel_repository.save_hotel(hotel=hotel)

    def __calculate_means_of_opinions(self, hotel_reviews:Sequence[Review])-> float:
        hotel_puntuations = []
        for review in hotel_reviews:
            hotel_puntuations.append(review.review)

        hotel_review_average = sum(hotel_puntuations) / len(hotel_puntuations)
        return hotel_review_average
