from requests import request


class RequestWrapper:
    """Generic wrapper for HTTP requests."""
    def __init__(self):
        """Attributes that will be used on basic functions.

        By default,
        The response of last request.
        The endpoint of last request.
        """
        self._response = None
        self._endpoint = None

    def set_end_point(self, value):
        """Setter for endpoint attribute."""
        self._endpoint = value

    def do_request(self, http_type, headers=None, params=None, data=None):
        """Execute the http request based on a type and given params.

        :param http_type: GET, POST, PUT, DELETE.
        :param headers: for request, by default no data required.
        :param params: for request, by default no data required.
        :param data: for request, by default no data required.
        :return: True.
        """
        self._response = request(http_type, self._endpoint, headers=headers,
                                 params=params, data=data)
        return True

    def get_json(self):
        """Getter for response as a json."""
        return self._response.json()

    def get_status(self):
        """Get status code for last http request."""
        return str(self._response.status_code)
