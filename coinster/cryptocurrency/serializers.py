from rest_framework import serializers
from .models import CryptoCurrency


class CryptocurrencyRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model   = CryptoCurrency
        exclude = [
                    'created_at',
                    'deleted_at',
                  ]
        
