from requests import request


class RequestWrapper:
    def __init__(self):
        self._response = None
        self._endpoint = None

    def set_end_point(self, value):
        self._endpoint = value

    def do_request(self, http_type, headers=None, params=None, data=None):
        self._response = request(http_type, self._endpoint, headers=headers, params=params, data=data)

    def get_json(self):
        return self._response.json()

    def get_status(self):
        return str(self._response.status_code)
