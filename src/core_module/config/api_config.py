

class ApiConfig:
    def __init__(self, google_api_sleep):
        self.__google_api_sleep = google_api_sleep

    @property
    def google_api_sleep(self):
        return self.__google_api_sleep
