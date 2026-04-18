import requests
import time
from utils.logger import get_logger

class BaseAPIClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json"
        }
        self.logger = get_logger()


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
    
    def get(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"

        start = time.time()

        response = requests.get(url, headers=headers)

        duration = round(time.time() - start, 3)

        self.logger.info(
            f"GET | {url} | {response.status_code} | {duration}"
        )
        return response
    
    def post(self, endpoint, data, headers=None):
        url = f"{self.base_url}{endpoint}"

        start = time.time()
        response = requests.post(url, json=data, headers=headers)
        duration = round(time.time() - start, 3)

        self.logger.info(f"POST | {url} | {response.status_code} | {duration}s")

        return response