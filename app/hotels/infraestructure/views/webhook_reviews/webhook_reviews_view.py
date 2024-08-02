import json
from datetime import datetime
from decimal import Decimal
from uuid import uuid4

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from hotels.application.add_reviews.add_review_command import AddReviewCommand
from hotels.application.add_reviews.add_review_command_handler import AddReviewCommandHandler
from hotels.domain.review_creator import ReviewCreator
from hotels.infraestructure.db_hotel_repository import DbHotelRepository
from hotels.infraestructure.db_review_repository import DbReviewRepository


@method_decorator(csrf_exempt, name="dispatch")
class WebhookReviewsView(View):
    def __init__(self):
        super().__init__()
        self.__db_review_repository = DbReviewRepository()
        self.__review_creator = ReviewCreator()
        self.__db_hotel_repository = DbHotelRepository()
        self.__add_reviews_command_handler = AddReviewCommandHandler(review_repository=self.__db_review_repository, review_creator=self.__review_creator, hotel_repository=self.__db_hotel_repository)


    def post(self, request):
        data = json.loads(request.body)
        review_uuid = uuid4()
        command = AddReviewCommand(
            review_uuid=review_uuid,
            hotel_name=data.get("hotel_name"),
            user_name=data.get("user_name"),
            review=Decimal(data.get("review")),
            title=data.get("title"),
            text=data.get("text"),
            published_at=datetime.strptime(data.get("published_at"), "%Y-%m-%d").date()
        )
        self.__add_reviews_command_handler.handle(command)
        return JsonResponse({'review_uuid': str(review_uuid)}, status=201)