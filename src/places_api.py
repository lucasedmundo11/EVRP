import json
import requests

class PlacesAPI:

    def __init__(self, city, base_url, api_key, maxResultCount, pageToken=None):
        self.base_url = base_url
        self.api_key = api_key
        self.status = None
        self.headers = {
            "Content-Type": "application/json",
            "X-Goog-Api-Key": api_key,
            "X-Goog-FieldMask": "places.location,places.evChargeOptions,places.addressComponents,nextPageToken"
        }
        self.payload = {
            "textQuery": f"charging station in {city}, São Paulo",
            "maxResultCount": maxResultCount,
        }
        if pageToken:
            self.payload["pageToken"] = pageToken

    def post(self):
        url = f"{self.base_url}"
        response = requests.post(url, headers=self.headers, json=self.payload)
        return self._handle_response(response)

    def _handle_response(self, response):
        self.status = response.status_code
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()


