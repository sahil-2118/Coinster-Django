from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
import django
django.setup()
from cryptocurrency.models import CryptoCurrency
from urllib.parse import parse_qs
from django.db.models import Q
from django.utils import timezone
from scheduler.models import Scheduler
from cryptocurrency.serializers import CryptocurrencyModelSerializer
from scheduler.serializers import SchedulerSerializer
import asyncio


class SchedulerConsumer(AsyncJsonWebsocketConsumer):
    @database_sync_to_async
    def check_scheduler(self, owner, crypto_id):
        now = timezone.now()
        schechedulers = Scheduler.objects.filter(owner=owner).filter(crypto=crypto_id)
        active_schedulers = schechedulers.filter(
            Q(activated_at__lte = now) & Q(expaired_at__gte = now)
        )
        if active_schedulers.exists():
            serialized = SchedulerSerializer(active_schedulers.first()) 
            return True, int(serialized.data.get("time_range"))
    
        return False, None

    @database_sync_to_async
    def get_crypto(self, symbol):
        try:
            crypto = CryptoCurrency.objects.get(symbol=symbol)
        except CryptoCurrency.DoesNotExist:
            crypto = None
        if crypto is not None:
            return crypto, crypto.id
        return None, None


    async def check_is_valid_request(self, symbol, user):
        task = asyncio.create_task(self.get_crypto(symbol))
        content, crypto_id = await task
        task1 = asyncio.create_task(self.check_scheduler(user, crypto_id))
        exist, time_range = await task1
        if self.scope.get('user').is_authenticated & (content is not None) & exist:
            return True, content, time_range
        return False, None, None
    
    async def connect(self):
        query_string = self.scope["query_string"]
        query_params = query_string.decode()
        query_dict = parse_qs(query_params)
        symbol = query_dict["coin"][0]
        is_ok, content, time_range = await self.check_is_valid_request(symbol, self.scope.get('user'))
        print('yesss', is_ok)
        if is_ok:
            await self.accept()
            while True:
                await self.send_json(content)
                await asyncio.sleep(time_range)
        else:
            self.close()

    async def send_json(self, content, close=False):
        exist, _ = await self.check_scheduler(self.scope.get('user'), content)
        print(exist)
        if exist:
            content = CryptocurrencyModelSerializer(content).data
            return await super().send_json(content, close=close)
        else:
            self.close()


    
    async def disconnect(self, close_code):
        await self.close()


    async def receive(self, text_data):
        await self.send_json({
            "message": "text data"
        })