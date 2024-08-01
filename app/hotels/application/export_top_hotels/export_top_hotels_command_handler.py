from cqrs.commands.command_handler import CommandHandler
from hotels.application.export_top_hotels.export_top_hotels_command import ExportTopHotelsCommand
from hotels.domain.hotel_repository import HotelRepository
import csv

class ExportTopHotelsCommandHandler(CommandHandler):
    def __init__(self, hotel_repository: HotelRepository):
        self.hotel_repository = hotel_repository

    def handle(self, command: ExportTopHotelsCommand):
        # obtener los hoteles
        hotels = self.hotel_repository.get_all_hotels()

        # parsear hoteles
        with open('top_hotels.csv', 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=',')
            csv_writer.writerow(['ID', 'Name', 'Address', 'Rating', 'City', 'Amenities'])
            for hotel in hotels:
                if hotel.rating >= 3.0:
                    csv_writer.writerow([
                        hotel.id,
                        hotel.hotel_name,
                        hotel.address,
                        hotel.rating,
                        hotel.city,
                        hotel.amenity,
                    ])

        # enviar mail



