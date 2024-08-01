

from config import settings
from cqrs.commands.command_handler import CommandHandler
from hotels.application.export_top_hotels.export_top_hotels_command import ExportTopHotelsCommand
from hotels.domain.hotel_repository import HotelRepository
import csv
from django.core.mail import send_mail
from django.core.mail import EmailMessage




class ExportTopHotelsCommandHandler(CommandHandler):
    def __init__(self, hotel_repository: HotelRepository):
        self.hotel_repository = hotel_repository


    def handle(self, command: ExportTopHotelsCommand):
        hotels = self.hotel_repository.filter_hotels_by_rating_gte(rating=3.0)

        csv_file_path = 'top_hotels.csv'
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=',')
            csv_writer.writerow(['ID', 'Name', 'Address', 'Rating', 'City', 'Amenities'])
            for hotel in hotels:
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













# # Enviar correo
#             email = EmailMessage(
#                 subject='Hoteles Recomendados',
#                 body='Adjunto encontrarás el archivo con la lista de hoteles recomendados.',
#                 from_email=settings.DEFAULT_FROM_EMAIL,
#                 to=['antoniaherrera620@gmail.com'],
#             )
#             email.attach_file(hotels_csv)
#             email.send(fail_silently=False)




