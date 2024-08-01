from config import settings
from cqrs.commands.command_handler import CommandHandler
from hotels.application.export_top_hotels.export_top_hotels_command import ExportTopHotelsCommand
from hotels.domain.exceptions.hotels_by_rating_not_found_exception import HotelsByRatingNotFoundException
from hotels.domain.hotel_repository import HotelRepository
import csv
from django.core.mail import EmailMessage




class ExportTopHotelsCommandHandler(CommandHandler):
    def __init__(self, hotel_repository: HotelRepository):
        self.hotel_repository = hotel_repository

    def handle(self, command: ExportTopHotelsCommand):
        top_hotels = self.hotel_repository.filter_hotels_by_rating_gte(rating=command.rating_gte)
        if len(top_hotels) == 0:
            raise HotelsByRatingNotFoundException(raiting=command.rating_gte)
        csv_file_path = 'top_hotels.csv'
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=',')
            csv_writer.writerow(['ID', 'Name', 'Address', 'Rating', 'City', 'Amenities'])
            for hotel in top_hotels:
                    csv_writer.writerow([
                        hotel.id,
                        hotel.hotel_name,
                        hotel.address,
                        hotel.rating,
                        hotel.city,
                        hotel.amenity,
                    ])

        # Enviar el email
        email = EmailMessage(
            "Informe semanal",
            "Adjunto tiene un informe donde observará los mejores hoteles del sistema",
            settings.DEFAULT_FROM_EMAIL,
            ["antoniaherrera620@gmail.com"],
        )
        email.attach_file(csv_file_path)
        email.send()
