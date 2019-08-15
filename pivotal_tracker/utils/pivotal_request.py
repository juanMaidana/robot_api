from core.utils.request_wrapper import RequestWrapper


class PivotalRequest(RequestWrapper):
    """Requests for Pivotal Tracker API
    Pivotal Tracker API requests have some specifications different from generic
    """
    def __init__(self):
        RequestWrapper.__init__(self)

    def build_end_point(self, url, *ids):
        """Specific way to build end points on Pivotal Tracker"""
        for index, value in enumerate(ids):
            url = url.replace('$ID('+str(index)+')', str(value))
        self._endpoint = url
