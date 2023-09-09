from .models import Scheduler
from .serializers import SchedulerRequestSerializer, SchedulerResponseSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import (DjangoModelPermissions,
                                        IsAdminUser,)


class SchedulerList(mixins.ListModelMixin, 
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    
    queryset = Scheduler.objects.all()
    permission_classes = [DjangoModelPermissions|IsAdminUser]
    

    def get(self, request, *args, **kwargs):
        self.serializer_class = SchedulerResponseSerializer
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        self.serializer_class = SchedulerRequestSerializer
        return self.create(request, *args, **kwargs)
    
    def has_permission(self, request, obj):
        return obj.user == request.user
        
    

class SchedulerDetail(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      generics.GenericAPIView):
    
    queryset = Scheduler.objects.all()
    serializer_class = SchedulerResponseSerializer
    permission_classes = [DjangoModelPermissions|IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        self.serializer_class = SchedulerResponseSerializer
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def has_permission(self, request, obj):
        return obj.user == request.user