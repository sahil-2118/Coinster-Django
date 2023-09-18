from rest_framework import serializers
from user.models import User
from cryptocurrency.models import CryptoCurrency
from .models import Scheduler
from django.utils import timezone
from datetime import  timedelta
from rest_framework.validators import UniqueTogetherValidator


class SchedulerResponseSerializer(serializers.Serializer):
    
    id = serializers.IntegerField()
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    crypto = serializers.HyperlinkedRelatedField(view_name="crypto_detail", read_only=True)
    activated_at = serializers.DateTimeField()
    expaired_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    
class SchedulerRequestSerializer(serializers.Serializer):
   
   time_range = serializers.IntegerField()
   owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
   crypto = serializers.PrimaryKeyRelatedField(queryset=CryptoCurrency.objects.all(),)
   activated_at = serializers.DateTimeField(required=False, default=timezone.now())
   expaired_at = serializers.DateTimeField(required=False, default=timezone.now() + timedelta(days=1))

   validators = [
            UniqueTogetherValidator(
                queryset=Scheduler.objects.all(),
                fields=['owner', 'crypto']
            )
        ]


   def create(self, validated_data):
       return Scheduler.objects.create(**validated_data)
   

   def update(self, instance, validated_data):
        instance.time_range = validated_data.get('time_range', instance.time_range)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.crypto = validated_data.get('crypto', instance.crypto)
        instance.activated_at = validated_data.get('activated_at', instance.activated_at)
        instance.expaired_at = validated_data.get('expaired_at', instance.expaired_at)
        instance.save()
        return instance
   
   def validate(self, attrs):
       if attrs.get('activated_at') >= attrs.get('expaired_at'):
           raise serializers.ValidationError('Activate date should be smaller than expiration date')
       else:
           return attrs
       
    
class SchedulerSerializer(serializers.Serializer):

   time_range = serializers.IntegerField()
   owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
   crypto = serializers.PrimaryKeyRelatedField(queryset=CryptoCurrency.objects.all(),)
