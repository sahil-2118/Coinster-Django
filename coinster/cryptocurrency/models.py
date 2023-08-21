from django.db import models


class CryptoCurrency(models.Model):

    name                = models.CharField(
                                            max_length=50,
                                        )
    symbol              = models.CharField(
                                            max_length=50,
                                        )
    rank                = models.PositiveSmallIntegerField()
    price               = models.DecimalField(
                                            max_digits=13,
                                            decimal_places=4,
                                            default=0,
                                            )
    circulating_supply  = models.BigIntegerField(
                                            null=True,
                                            blank=True,
                                            )
    volume_24h          = models.BigIntegerField()
    percent_change_24h  = models.FloatField(
                                            null=True,
                                            blank=True,
                                            )
    percent_change_1h   = models.FloatField(
                                            null=True,
                                            blank=True,
                                            )
    percent_change_7d   = models.FloatField(
                                            null=True,
                                            blank=True,
                                            )
    market_cap          = models.FloatField()
    last_update         = models.DateTimeField(
                                            auto_now=True,
                                            )
    created_at          = models.DateTimeField(
                                            auto_now_add=True,
                                            )
    deleted_at          = models.DateTimeField(
                                            null=True,
                                            )

    class Meta:
        ordering = ["rank"]
        verbose_name_plural = "cryptocurrencies"
        indexes = [
            models.Index(fields=["rank",]),
            models.Index(fields=["symbol",]),
            models.Index(fields=["created_at",]),
            ]
    







