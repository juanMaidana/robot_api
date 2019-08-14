from requests import request


class RequestWrapper:
    def __init__(self):
        self.__response = None
        self.__endpoint = ''

    def set_end_point(self, value):
        self.__endpoint = value

    def do_request(self, http_type, headers=None, params=None):
        self.__response = request(http_type, self.__endpoint, headers=headers, params=params)

    def get_json(self):
        return self.__response.json()

    def get_status(self):
        return self.__response.status_code
