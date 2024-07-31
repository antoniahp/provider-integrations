class HotelByNameNotFoundException(Exception):
    def __init__(self, hotel_name: str) -> None:
        self.hotel_name = hotel_name
        self.message = f"The hotel {hotel_name} does not exist."
        super().__init__(self.message)