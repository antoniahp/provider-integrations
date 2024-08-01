from django.core.management import BaseCommand

from hotels.application.export_top_hotels.export_top_hotels_command import ExportTopHotelsCommand
from hotels.application.export_top_hotels.export_top_hotels_command_handler import ExportTopHotelsCommandHandler
from hotels.infraestructure import db_hotel_repository
from hotels.infraestructure.db_hotel_repository import DbHotelRepository


class Command(BaseCommand):
    help="Export top hotels"

    def __init__(self):
        super().__init__()
        self.__db_hotel_repository = DbHotelRepository()
        self.__export_top_hotels_command_handler = ExportTopHotelsCommandHandler(hotel_repository=self.__db_hotel_repository)

    def handle(self, *args, **options):
        command=ExportTopHotelsCommand()
        self.__export_top_hotels_command_handler.handle(command)