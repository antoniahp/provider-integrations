from cqrs.commands.command_handler import CommandHandler
from hotels.application.import_hotels_provider_a.import_hotels_provider_a_comand import ImportHotelsProviderACommand
from hotels.domain.hotel import Hotel

from hotels.domain.hotel_repository import HotelRepository
import requests


class ImportHotelsProviderACommandHandler(CommandHandler):
    def __init__(self, hotel_repository: HotelRepository):
        self.hotel_repository = hotel_repository

    def handle(self, command: ImportHotelsProviderACommand):
        #hacer peticion a proveedor
        hotels_provider_a = requests.get("https://raw.githubusercontent.com/adriancast/api/main/hotel-provider-A")
        json_response = hotels_provider_a.json()
        # extraer objetos boteles de la respuesta del proveedor
        parsed_hotels = []
        for hotel in json_response["data"]["hotels"]:
            parsed_hotels.append(
                Hotel(
                provider_id=hotel["id"],
                hotel_name=hotel["label"],
                address=hotel["address"],
                rating=hotel["rating"],
                availability=hotel["rooms_available"],
                price_per_night=hotel["price_per_night"],
                city=""
            ))

        #guardar hotel sino estan en la bbdd, filtramos y sino obtengo resultados lo guardo
        for hotel in parsed_hotels:
            hotels_filtered_by_name = self.hotel_repository.filter_hotels_by_name(hotel.hotel_name)
            if len(hotels_filtered_by_name) == 0:
                self.hotel_repository.save_hotel(hotel)
