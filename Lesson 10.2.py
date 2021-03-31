import time
import requests
import os

token = ""
file_path = ""


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        response = requests.put(self._get_upload_link(file_path), data=open(file_path, "rb"), timeout=5)
        if response.status_code == 201:
            return "Success"

    def _get_file_name(self, file_path):
        return os.path.basename(file_path)

    def _get_headers(self):
        return {"Content-type": "application/json", "Authorization": f"OAuth {self.token}"}

    def _get_upload_link(self, file_path):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {"path": self._get_file_name(file_path), "overwrite": "true"}
        response = requests.get(url, params=params, headers=self._get_headers(), timeout=5)
        time.sleep(0.3)
        return response.json()["href"]


uploader = YaUploader(token)
print(uploader.upload(file_path))
