import requests

class BaseAPIClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json"
        }

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=self.headers)
        return response

    def post(self, endpoint, data):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, json=data, headers=self.headers)
        return response
    
    def get(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=headers)
        return response

    def post(self, endpoint, data, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, json=data, headers=headers)
        return response