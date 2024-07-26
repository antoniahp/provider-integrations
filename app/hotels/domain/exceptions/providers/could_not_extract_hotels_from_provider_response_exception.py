class CouldNotExtracHotelsFromProviderResponseException(Exception):
    def __init__(self, provider_name:str) -> None:
        self.provider_name = provider_name
        self.provider_message = f"Couldn't extract hotels from provier {provider_name}"
        super().__init__(self.provider_message)