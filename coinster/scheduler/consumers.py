from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
import django
django.setup()
from cryptocurrency.models import CryptoCurrency
from urllib.parse import parse_qs
from django.db.models import Q
from django.utils import timezone
from scheduler.models import Scheduler
import asyncio

@database_sync_to_async
def get_crypto(symbol):
    try:
        crypto = CryptoCurrency.objects.get(symbol=symbol)
    except CryptoCurrency.DoesNotExist:
        crypto = None
    return crypto

@database_sync_to_async
def check_scheduler(owner, crypto):
    now = timezone.now()
    schechedulers = Scheduler.objects.filter(owner=owner).filter(crypto=crypto)
    active_schedulers = schechedulers.filter(
        Q(activated_at__lte = now) & Q(expaired_at__gte = now)
    )
    if active_schedulers.exists():
        return True
    
    return False
        
        

class SchedulerConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        query_string = self.scope["query_string"]
        query_params = query_string.decode()
        query_dict = parse_qs(query_params)
        symbol = query_dict["coin"][0]
        self.scope['crypto'] = get_crypto(symbol)
        if self.scope.get('user').is_authenticated & (self.scope['crypto'] is not None):
            await self.accept()
        else:
            raise ValueError("You are not log in or coin is invalid")

    
    async def send_json(self, content, close=False):
        if check_scheduler(self.scope.get('user'), self.scope.get('crypto')):
            return await super().send_json(content, close=close)
        else:
            print("Error sending")
            raise ValueError("You don't have scheduler")
        
    
    # async def receive_json(self, content):
    #     print('hello')
    #     await self.send_json(content)
    #     asyncio.sleep(5)
    #     await self.send_json(content)
            

    
    async def disconnect(self, close_code):
        await self.close()


    async def receive(self, text_data):
        print('hello')
        await self.send_json(text_data)
        await asyncio.sleep(5)
        await self.send_json(text_data)