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
        fetched_data['symbol'] = data.get('symbol', 'undefined')
        fetched_data['rank'] = data.get('cmc_rank', 'undefined')
        fetched_data['circulating_supply'] = data.get('circulating_supply', 'undefined')
        fetched_data['price'] = round(data.get('quote').get('USD').get('price', 'undefined'), 4)
        fetched_data['volume_24h'] = data.get('quote').get('USD').get('volume_24h', 'undefined')
        fetched_data['percent_change_24h'] = data.get('quote').get('USD').get('percent_change_24h', 'undefined')
        fetched_data['percent_change_1h'] = data.get('quote').get('USD').get('percent_change_1h', 'undefined')
        fetched_data['percent_change_7d'] =data.get('quote').get('USD').get('percent_change_7d', 'undefined')
        fetched_data['market_cap'] = data.get('quote').get('USD').get('market_cap', 'undefined')
        return fetched_data
    
    def create(self, validated_data):
        created, _ =CryptoCurrency.objects.update_or_create(**validated_data)
        return created
        