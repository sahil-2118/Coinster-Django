from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

from cryptocurrency.models import CryptoCurrency

User = get_user_model()

class Scheduler(models.Model):

    time_range  = models.BigIntegerField(
                                verbose_name=_("""
                                               this is time range for store the range of time that user want to send data
                                               """),
                                )
    owner       = models.ForeignKey(
                                to = User,
                                verbose_name=_("the owner of scheduler"),
                                related_name="schedulers",
                                on_delete=models.CASCADE,
                            )
    crypto      = models.ForeignKey(
                                to = CryptoCurrency,
                                verbose_name=_("the crypto of scheduler"),
                                related_name="schedulers",
                                on_delete=models.CASCADE,
                            )
    created_at  = models.DateTimeField(
                                auto_now_add=True,
                                )
    updated_at  = models.DateTimeField(
                                auto_now=True,
                                )
    deleted_at  = models.DateTimeField(
                                null=True,
                                )
    class Meta:
       ordering = ["-created_at"]
       verbose_name_plural = "schedulers"
       indexes =[
           models.Index(fields=["owner",]),
           models.Index(fields=["created_at",]),
       ] 



