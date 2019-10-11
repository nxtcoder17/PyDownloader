import requests

class ParseUrl:
    def __init__(self, url):
        self.url = url

    def extract_info(self):
        response = requests.get(self.url,  stream=True)
        data = dict()
        try:
            data['content-length'] = int (response.headers['content-length'])
        except KeyError:
            data['content-length'] = None

        return data
