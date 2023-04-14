import urllib.parse as urlparse


class UrlBuilder:
    def __init__(self, base: str, params: dict):
        self.base = base
        self.params = params
        self.extra_params = {}

    def add_params(self, **params):
        self.extra_params = params

        return self

    def build(self):

        return self.base + "&" + urlparse.urlencode({**self.params, **self.extra_params})
