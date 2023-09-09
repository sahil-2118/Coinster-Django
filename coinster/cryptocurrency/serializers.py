from rest_framework import serializers
from .models import CryptoCurrency
from django.shortcuts import get_object_or_404


class CryptocurrencyModelSerializer(serializers.ModelSerializer):

    class Meta:
        model   = CryptoCurrency
        exclude = [
                    'created_at',
                    'deleted_at',
                  ]
        read_only_fields = ["id", "last_updated"]

    



class CryptocurrencyCreateOrUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model   = CryptoCurrency
        exclude = [
                    'id',
                    'last_update',
                    'created_at',
                    'deleted_at',
                  ]

    def to_internal_value(self, data):
        fetched_data = {}
        fetched_data['name'] = data.get('name', 'undefined')
        fetched_data['symbol'] = data['symbol']
        fetched_data['rank'] = data['cmc_rank']
        fetched_data['circulating_supply'] = data['circulating_supply']
        fetched_data['price'] = round(data['quote']['USD']['price'], 4)
        fetched_data['volume_24h'] = data['quote']['USD']['volume_24h']
        fetched_data['percent_change_24h'] = data['quote']['USD']['percent_change_24h']
        fetched_data['percent_change_1h'] = data['quote']['USD']['percent_change_1h']
        fetched_data['percent_change_7d'] = data['quote']['USD']['percent_change_7d']
        fetched_data['market_cap'] = data['quote']['USD']['market_cap']
        return super().to_internal_value(fetched_data)
    
    def create(self, validated_data):
        if CryptoCurrency.objects.filter(symbol=validated_data['symbol']).exists():
            print('ok')
            #crypto = CryptoCurrency.objects.filter(symbol=validated_data['symbol']).update(**validated_data)
            #return super().update(**validated_data)
        else:
            print('not ok')
            return CryptoCurrency.objects.create(**validated_data)
        