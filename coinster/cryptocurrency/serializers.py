from rest_framework import serializers
from .models import CryptoCurrency


class CryptocurrencyModelSerializer(serializers.ModelSerializer):

    class Meta:
        model   = CryptoCurrency
        exclude = [
                    'created_at',
                    'deleted_at',
                  ]
        read_only_fields = ["id", "last_updated"]


