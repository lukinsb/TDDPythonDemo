import requests


class requestTest:
    url = "test"

    def __init__(self, new_url):
        self.url = new_url

    def make_request(self):
        req = requests.get(self.url)
        return req.status_code
