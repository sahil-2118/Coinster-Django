from rest_framework import serializers
from scheduler.models import Scheduler
from .models import User

class UserSerializer(serializers.ModelSerializer):
    schedulers = serializers.PrimaryKeyRelatedField(many=True, queryset=Scheduler.objects.all())
    class Meta:
        model = User
        fields=['id', 'username', 'schedulers']