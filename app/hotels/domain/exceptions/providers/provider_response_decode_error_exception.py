class ProviderResponseDecodeErrorException(Exception):
    def __init__(self, provider_name:str) -> None:
        self.provider_name = provider_name
        self.message = f"Could not decode response from provider {provider_name} ."
        super().__init__(self.message)