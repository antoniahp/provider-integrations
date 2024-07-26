from django.core.management import BaseCommand

from hotels.application.import_hotels_provider_b.import_hotels_provider_b_command import ImportHotelsProviderBCommand
from hotels.application.import_hotels_provider_b.import_hotels_provider_b_command_handler import ImportHotelsProviderBCommandHandler
from hotels.domain.hotel_creator import HotelCreator
from hotels.infraestructure.db_hotel_repository import DbHotelRepository


class Command(BaseCommand):
    help = "Import hotels provider B"

    def __init__(self):
        super().__init__()
        self.__db_hotel_repository = DbHotelRepository()
        self.__hotel_creator = HotelCreator()
        self.__import_hotels_provider_b_command_handler = ImportHotelsProviderBCommandHandler(hotel_creator=self.__hotel_creator, hotel_repository=self.__db_hotel_repository)

    def handle(self, *args, **options):
        command = ImportHotelsProviderBCommand()
        self.__import_hotels_provider_b_command_handler.handle(command)
