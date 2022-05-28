

class GoogleApiConfig:
    def __init__(self, api_sleep, max_message_len, max_len_error_message):
        self.__api_sleep = api_sleep
        self.__max_message_len = max_message_len
        self.__max_len_error_message = max_len_error_message

    @property
    def api_sleep(self):
        return self.__api_sleep

    @property
    def max_message_len(self):
        return self.__max_message_len

    @property
    def max_len_error_message(self):
        return self.__max_len_error_message
