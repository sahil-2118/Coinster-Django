from rest_framework import serializers
from user.models import User
from cryptocurrency.models import CryptoCurrency
from .models import Scheduler

class SchedulerRequestSerializer(serializers.Serializer):
    
    id = serializers.IntegerField()
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    crypto = serializers.HyperlinkedRelatedField(view_name="crypto_detail", read_only=True)
    updated_at = serializers.DateTimeField()
    
class SchedulerResponseSerializer(serializers.Serializer):
   
   time_range = serializers.IntegerField()
   owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
   crypto = serializers.PrimaryKeyRelatedField(queryset=CryptoCurrency.objects.all())


   def create(self, validated_data):
       return Scheduler.objects.create(**validated_data)
   

   def update(self, instance, validated_data):
        instance.time_range = validated_data.get('time_range', instance.time_range)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.crypto = validated_data.get('crypto', instance.crypto)
        instance.save()
        return instance


