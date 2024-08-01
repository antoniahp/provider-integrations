class HotelsByRatingNotFoundException(Exception):
    def __init__(self, raiting: float):
        self.raiting = raiting
        self.message = f"We do not have hotels with an average higher than {raiting}"
        super().__init__(self.message)