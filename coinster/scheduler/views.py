from .models import Scheduler
from .serializers import (SchedulerRequestSerializer, 
                          SchedulerResponseSerializer,
                          SchedulerSerializer,
                          )
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import (DjangoModelPermissions,
                                        IsAdminUser,
                                        IsAuthenticated,
                                        SAFE_METHODS)
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from cryptocurrency.models import CryptoCurrency
from django.utils import timezone


class SchedulerList(mixins.ListModelMixin, 
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    
    queryset = Scheduler.objects.all()
    

    def get(self, request, *args, **kwargs):
        self.serializer_class = SchedulerResponseSerializer
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        fetch_owner(request)
        fetch_crypto(request)
        self.serializer_class = SchedulerRequestSerializer
        return self.create(request, *args, **kwargs)
    
    def has_permission(self, request, obj):
        return obj.owner == request.user
    
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return (DjangoModelPermissions(), IsAdminUser(),)
        else:
            return (IsAuthenticated(),)
        
    

class SchedulerDetail(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      generics.GenericAPIView):
    
    queryset = Scheduler.objects.all()
    serializer_class = SchedulerRequestSerializer
    permission_classes = [DjangoModelPermissions|IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        self.serializer_class = SchedulerResponseSerializer
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def has_permission(self, request, obj):
        return obj.owner == request.user
    

class SchedulerRequest(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        fetch_owner(request)
        fetch_crypto(request)
        serialized = SchedulerSerializer(data=request.data)
        if serialized.is_valid():
            now = timezone.now()
            schechedulers = Scheduler.objects.filter(owner=serialized.data.get('owner')).filter(crypto=serialized.data.get('crypto'))
            active_schedulers = schechedulers.filter(
                Q(activated_at__lte = now) & Q(expaired_at__gte = now)
            )
            if active_schedulers.exists():
                return Response({"message": "You've got a scheduler for these days."})
            else:

                return Response(serialized.data)
            
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)   


    

def fetch_owner(request):
        owner = Token.objects.get(key=request.auth)
        request.data['owner'] = owner.user_id


def fetch_crypto(request):
        value = request.data.get('crypto')
        if value.isnumeric():
            request.data['crypto'] = value
        else:
            crypto = CryptoCurrency.objects.get(symbol=value)
            request.data['crypto'] = crypto.id