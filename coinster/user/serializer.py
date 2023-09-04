from rest_framework import serializers
from scheduler.models import Scheduler
from .models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.validators import UnicodeUsernameValidator


class UserResponseSerializer(serializers.ModelSerializer):
    schedulers = serializers.PrimaryKeyRelatedField(many=True, queryset=Scheduler.objects.all())
    class Meta:
        model = User
        fields=['id', 'username', 'schedulers']

class UserRequestSerializer(serializers.Serializer):
    first_name = serializers.CharField(
                                        max_length=50, 
                                        required=False, 
                                        allow_blank=True,
                                        )
    last_name = serializers.CharField(
                                       max_length=80, 
                                       required=False, 
                                       allow_blank=True,
                                       )
    email = serializers.EmailField(
                                       required=False, 
                                       allow_blank=True,
                                       validators=[UniqueValidator(queryset=User.objects.all()),],
                                    )
    username = serializers.CharField(
                                       max_length=150,
                                       validators=[UniqueValidator(queryset=User.objects.all()),
                                                   UnicodeUsernameValidator(),],
    )
    password = serializers.CharField(
                                       max_length=8,
                                       min_length=4,
    )


    def create(self, validated_data):
       return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance



