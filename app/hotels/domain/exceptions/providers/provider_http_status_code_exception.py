class ProviderHttpStatusCodeException(Exception):
    def __init__(self, status_code: int, provider_name:str) -> None:
        self.status_code = status_code
        self.provider_name = provider_name
        self.message = f"The provider {provider_name} has returned code error {status_code} ."
        super().__init__(self.message)