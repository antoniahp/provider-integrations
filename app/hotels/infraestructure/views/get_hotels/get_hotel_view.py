from django.http import JsonResponse
from django.views import View

from hotels.application.get_hotels.get_hotels_query import GetHotelsQuery
from hotels.application.get_hotels.get_hotels_query_handler import GetHotelsQueryHandler
from hotels.infraestructure.db_hotel_repository import DbHotelRepository

from hotels.infraestructure.views.get_hotels.get_hotel_serializer import GetHotelSerializer


class GetHotelView(View):
    def __init__(self):
        self.__hotel_repository = DbHotelRepository()
        self.__get_hotels_query_handler = GetHotelsQueryHandler(hotel_repository = self.__hotel_repository)
        self.__get_hotel_serializer = GetHotelSerializer()

    def get(self,request):

        query = GetHotelsQuery()
        query_response = self.__get_hotels_query_handler.handle(query)
        hotels = query_response.content
        return JsonResponse({
            "hotels": self.__get_hotel_serializer.serialize(hotels)
        }, status=200)