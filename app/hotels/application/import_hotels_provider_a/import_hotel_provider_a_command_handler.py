from typing import Dict, List

from cqrs.commands.command_handler import CommandHandler
from hotels.application.import_hotels_provider_a.import_hotels_provider_a_comand import ImportHotelsProviderACommand
from hotels.domain.exceptions.providers.could_not_extract_hotels_from_provider_response_exception import CouldNotExtracHotelsFromProviderResponseException
from hotels.domain.exceptions.providers.provider_http_status_code_exception import ProviderHttpStatusCodeException
from hotels.domain.exceptions.providers.provider_response_decode_error_exception import ProviderResponseDecodeErrorException
from hotels.domain.exceptions.providers.provider_timeout_exception import ProviderTimeoutException
from hotels.domain.hotel import Hotel

from hotels.domain.hotel_repository import HotelRepository
import requests


class ImportHotelsProviderACommandHandler(CommandHandler):
    def __init__(self, hotel_repository: HotelRepository):
        self.hotel_repository = hotel_repository

    def handle(self, command: ImportHotelsProviderACommand):
        provider_response = self.__make_request_to_provider()
        hotels = self.__get_hotels_from_response(json_response=provider_response)
        self.__save_hotels_to_repository_only_if_its_new(parsed_hotels=hotels)


    def __make_request_to_provider(self) -> dict:
        try:
            hotels_provider_a = requests.get("https://raw.githubusercontent.com/adriancast/api/main/hotel-provider-A", timeout=20)
        except requests.exceptions.Timeout:
            raise ProviderTimeoutException(timeout=20, provider_name="hotel-provider-A")

        try:
            hotels_provider_a.raise_for_status()
        except requests.exceptions.HTTPError:
            raise ProviderHttpStatusCodeException(status_code=hotels_provider_a.status_code, provider_name="hotel-provider-A")

        try:
            json_response = hotels_provider_a.json()
        except requests.exceptions.JSONDecodeError:
            raise ProviderResponseDecodeErrorException(provider_name="hotel-provider-A")

        return json_response

    def __get_hotels_from_response(self, json_response:dict) -> List[Hotel]:
        parsed_hotels = []
        for hotel in json_response["hotels"]:
            try:
                parsed_hotels.append(
                    Hotel(
                    provider_id=hotel["id"],
                    hotel_name=hotel["details"]["name"],
                    address=hotel["details"]["address"],
                    rating=hotel["details"]["rating"],
                    availability=hotel["availability"]["rooms_available"],
                    price_per_night=hotel["availability"]["price_per_night"],
                    city=""
                ))
            except KeyError:
                raise CouldNotExtracHotelsFromProviderResponseException(provider_name="hotel-provider-A")
        return parsed_hotels

    def __save_hotels_to_repository_only_if_its_new(self, parsed_hotels:List[Hotel]) -> None:
        for hotel in parsed_hotels:
            hotels_filtered_by_name = self.hotel_repository.filter_hotels_by_name(hotel.hotel_name)
            if len(hotels_filtered_by_name) == 0:
                self.hotel_repository.save_hotel(hotel)
