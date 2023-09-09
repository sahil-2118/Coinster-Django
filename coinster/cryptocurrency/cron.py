from requests import Request, Session
from dotenv import load_dotenv
import os
import json
from .models import CryptoCurrency
from .serializers import CryptocurrencyCreateOrUpdateSerializer
from requests.exceptions import (ConnectionError, 
                                 Timeout, 
                                 TooManyRedirects,)

load_dotenv()

def crypto_scheduler():
    url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'10',
      'convert':'USD',
    }    
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': os.environ.get('API_KEY'),
    }

    session = Session()
    session.headers.update(headers)

    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      if data['data']:
        for crypto in data['data']:
          print(crypto.get('symbol'))
          serialized = CryptocurrencyCreateOrUpdateSerializer(data=crypto)
          if serialized.is_valid():
            serialized.save()
            #created = CryptoCurrency.objects.update_or_create(serialized)
            print('success')
          else:
            print(serialized.errors)
      else:
        print(data['status'])
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)