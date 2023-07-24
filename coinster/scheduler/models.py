from django.db import models
from django.contrib.auth import get_user_model
from ..cryptocurrency.models import CryptoCurrency

User = get_user_model()

class Scheduler(models.Model):

    time_range = models.BigIntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    crypto = models.ForeignKey(CryptoCurrency, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

