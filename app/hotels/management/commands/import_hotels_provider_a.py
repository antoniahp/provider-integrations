from django.core.management import BaseCommand

from hotels.application.import_hotels_provider_a.import_hotels_provider_a_command_handler import ImportHotelsProviderACommandHandler
from hotels.application.import_hotels_provider_a.import_hotels_provider_a_comand import ImportHotelsProviderACommand
from hotels.domain.hotel_creator import HotelCreator
from hotels.infraestructure.db_hotel_repository import DbHotelRepository


class Command(BaseCommand):
    help = "Import hotels provider A"

    def __init__(self):
        super().__init__()
        self.__db_hotel_repository = DbHotelRepository()
        self.__hotel_creator = HotelCreator()
        self.__import_hotels_provider_a_command_handler = ImportHotelsProviderACommandHandler(hotel_repository=self.__db_hotel_repository, hotel_creator=self.__hotel_creator)

    def handle(self, *args, **options):
        command = ImportHotelsProviderACommand()
        self.__import_hotels_provider_a_command_handler.handle(command)
