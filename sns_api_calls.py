import requests
from datetime import datetime, timedelta


class SnsData:
    def __init__(self):
        self.base_url = "https://sns-api.bonfida.com"

    def get_last_sales(self, limit=10):
        last_sales_endpoint = f"/sales/last?limit={limit}"
        url = self.base_url + last_sales_endpoint
        return self._get_data(url)

    def get_category_stats(self, months=0):
        today = datetime.now()
        start_time = int((today - timedelta(days=30 * months)).timestamp())
        end_time = int(today.timestamp())

        category_stats_endpoint = f"/categories/stats?start_time={start_time}&end_time={end_time}"
        url = self.base_url + category_stats_endpoint
        return self._get_data(url)

    def get_registrations(self, months=0, limit=50):
        today = datetime.now()
        start_time = int((today - timedelta(days=30 * months)).timestamp())
        end_time = int(today.timestamp())

        registration_endpoint = f"/sales/registrations?limit={limit}&start_time={start_time}&end_time={end_time}"
        url = self.base_url + registration_endpoint
        return self._get_data(url)

    def get_leaderboard(self):
        leaderboard_endpoint = "/sales/leaderboard"
        url = self.base_url + leaderboard_endpoint
        return self._get_data(url)

    def _get_data(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    @staticmethod
    def round_prices(data):
        if data:
            keys_to_round = ['price', 'usd_price', 'min_sale', 'max_sale', 'avg_price', 'volume']
            for item in data.get('result', []):
                for key in keys_to_round:
                    if key in item and isinstance(item[key], (int, float)):
                        item[key] = "{:,.1f}".format(item[key])
        return data
