from core.utils.request_wrapper import RequestWrapper


class PivotalRequest(RequestWrapper):
    def __init__(self):
        RequestWrapper.__init__(self)

    def build_end_point(self, url, *ids):
        for index, value in enumerate(ids):
            url = url.replace('$ID('+str(index)+')', str(value))
        self._endpoint = url
