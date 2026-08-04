import requests
import time
from utils.logger import get_logger


class BaseAPIClient:
    """Centralized HTTP client for API testing."""

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.logger = get_logger(__name__)
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def _request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        start = time.time()
        response = self.session.request(method, url, **kwargs)
        duration = round(time.time() - start, 3)
        self.logger.info(f"{method.upper()} | {url} | {response.status_code} | {duration}s")
        return response

    def get(self, endpoint: str, **kwargs) -> requests.Response:
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, json=None, **kwargs) -> requests.Response:
        return self._request("POST", endpoint, json=json, **kwargs)

    def put(self, endpoint: str, json=None, **kwargs) -> requests.Response:
        return self._request("PUT", endpoint, json=json, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        return self._request("DELETE", endpoint, **kwargs)