from cqrs.queries.query_handler import QueryHandler
from cqrs.queries.query_response import QueryResponse
from hotels.application.get_hotel.get_hotel_query import GetHotelsQuery
from hotels.domain.hotel_repository import HotelRepository
from hotels.infraestructure.db_hotel_repository import DbHotelRepository


class GetHotelsQueryHandler(QueryHandler):
    def __init__(self, hotel_repository: HotelRepository):
        self.hotel_repository = hotel_repository

    def handle(self, query: GetHotelsQuery) -> QueryResponse:
        hotels = self.hotel_repository.get_all_hotels()
        return QueryResponse(content=hotels)