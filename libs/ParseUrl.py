import requests

class ParseUrl:
    def __init__(self, url):
        self.url = url

    def extract_info(self):
        response = requests.get(self.url,  stream=True)
        data = dict()
        for key in response.headers:
            if key.lower() == 'content-length':
                data['content-length'] = int(response.headers['content-length'])

        return data
