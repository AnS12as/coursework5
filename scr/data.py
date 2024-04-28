import requests


class HHParser:
    def __init__(self, session):
        self.session = session
        self.base_url = "https://api.hh.ru"

    def get_employers(self):
        response = self.session.get(f"{self.base_url}/employers")
        if response.status_code == 200:
            return response.json()['items']
        return []

    def filter_vacancies(self):
        response = self.session.get(f"{self.base_url}/vacancies")
        if response.status_code == 200:
            return response.json()['items']
        return []
