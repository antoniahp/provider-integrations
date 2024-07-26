from typing import List

import requests
from django.db import transaction

from cqrs.commands.command_handler import CommandHandler
from hotels.application.import_hotels_provider_b.import_hotels_provider_b_command import ImportHotelsProviderBCommand
from hotels.domain.exceptions.providers.could_not_extract_hotels_from_provider_response_exception import CouldNotExtracHotelsFromProviderResponseException
from hotels.domain.exceptions.providers.provider_http_status_code_exception import ProviderHttpStatusCodeException
from hotels.domain.exceptions.providers.provider_response_decode_error_exception import ProviderResponseDecodeErrorException
from hotels.domain.exceptions.providers.provider_timeout_exception import ProviderTimeoutException
from hotels.domain.hotel import Hotel
from hotels.domain.hotel_creator import HotelCreator
from hotels.domain.hotel_repository import HotelRepository


class ImportHotelsProviderBCommandHandler(CommandHandler):
    def __init__(self, hotel_repository: HotelRepository, hotel_creator: HotelCreator):
        self.hotel_repository = hotel_repository
        self.hotel_creator = hotel_creator


    def handle(self, command: ImportHotelsProviderBCommand):
        hotels_provider_b_response = self.__make_request_to_provider_b()
        hotels_provider_b = self.__get_hotels_from_response_provider_b(hotels_provider_b_response)
        with transaction.atomic():
            self.__save_hotels_to_repository_only_if_its_new(hotels_provider_b)

    def __make_request_to_provider_b(self) -> dict:
        try:
            hotels_provider_b = requests.get("https://raw.githubusercontent.com/adriancast/api/main/hotel-provider-B", timeout=30)
        except requests.exceptions.Timeout:
            raise ProviderTimeoutException(timeout=30, provider_name="hotel-provider-B")

        try:
            hotels_provider_b.raise_for_status()
        except requests.exceptions.HTTPError:
            raise ProviderHttpStatusCodeException(status_code=hotels_provider_b.status_code, provider_name="hotel-provider-B")

        try:
            hotels_provider_b_response = hotels_provider_b.json()
        except requests.exceptions.JSONDecodeError:
            raise ProviderResponseDecodeErrorException(provider_name="hotel-provider-B")

        return hotels_provider_b_response


    def __get_hotels_from_response_provider_b(self, hotels_provider_b_response: dict) -> List[Hotel]:
        hotels_provider_b = []
        for hotel in hotels_provider_b_response["data"]["hotels"]:
            try:
                hotels_provider_b.append(
                    self.hotel_creator.create(
                        provider_id=hotel["id"],
                        hotel_name=hotel["label"],
                        address=hotel["address"],
                        rating=hotel["rating"],
                        availability=hotel["rooms_available"],
                        price_per_night=hotel["price_per_night"],
                        city=""
                    )
                )
            except KeyError:
                raise CouldNotExtracHotelsFromProviderResponseException(provider_name="hotel-provider-B")
        return hotels_provider_b

    def __save_hotels_to_repository_only_if_its_new(self, hotels_provider_b: List[Hotel]) -> None:
        for hotel in hotels_provider_b:
            hotels_filtered_by_name = self.hotel_repository.filter_hotels_by_name(hotel.hotel_name)
            if len(hotels_filtered_by_name) == 0:
                self.hotel_repository.save_hotel(hotel)