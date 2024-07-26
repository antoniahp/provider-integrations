class ProviderTimeoutException(Exception):
    def __init__(self, timeout: int, provider_name:str) -> None:
        self.timeout = timeout
        self.provider_name = provider_name
        self.message = f"The provider {provider_name} has not responded in {timeout} seconds."
        super().__init__(self.message)


