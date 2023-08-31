import requests
from dotenv import load_dotenv
import os
from .models import CryptoCurrency
from .serializers import CryptocurrencyModelSerializer
from requests.exceptions import (ConnectionError, 
                                 Timeout, 
                                 TooManyRedirects,)

load_dotenv()

def crypto_scheduler():
    url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'5000',
      'convert':'USD',
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': os.environ.get('API_KEY'),
    }

    try:
        response = requests.get(url)
        json = response.json()
        if json['data']:
            data = CryptocurrencyModelSerializer(data=json['data'])
            json = CryptocurrencyModelSerializer(data)
            for crypto in json:
                CryptoCurrency.objects.update_or_create(crypto)
            else:
                print(json['status'])
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)