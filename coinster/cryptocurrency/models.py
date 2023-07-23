from django.db import models

class CryptoCurrency(models.Model):

    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=50)
    rank = models.IntegerField()
    circulating_supply = models.BigIntegerField()
    total_supply = models.BigIntegerField()
    volume_24h = models.IntegerField()
    percent_change_24h = models.FloatField()
    percent_change_1h = models.FloatField()
    percent_change_7d = models.FloatField()
    market_cap = models.FloatField()
    last_update = models.DateTimeField()