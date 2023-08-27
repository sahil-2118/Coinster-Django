from rest_framework import serializers
from user.models import User
from cryptocurrency.models import CryptoCurrency

class SchedulerRequestSerializer(serializers.Serializer):
    
    id = serializers.IntegerField()
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    crypto = serializers.HyperlinkedRelatedField(view_name="crypto-detail", read_only=True)
    updated_at = serializers.DateTimeField()
    
class SchedulerResponseSerializer(serializers.Serializer):
   
   time_range = serializers.DateTimeField()
   owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
   crypto = serializers.PrimaryKeyRelatedField(queryset=CryptoCurrency.objects.all())
