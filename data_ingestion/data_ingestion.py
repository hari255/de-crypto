import requests
import logging 


def retrive_key(api_key):
    API_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }
    try:
        # Making GET request
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

        # Parsing JSON
        data = response.json()
        return data['data']
    except requests.RequestException as e:
        logging.error(f"Error retrieving data from CoinMarketCap API: {e}")
        return None
