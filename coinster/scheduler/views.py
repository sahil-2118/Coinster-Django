from .models import Scheduler
from .serializers import SchedulerRequestSerializer, SchedulerResponseSerializer
from rest_framework import mixins
from rest_framework import generics

class SchedulerList(mixins.ListModelMixin, 
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    
    queryset = Scheduler.objects.all()
    

    def get(self, request, *args, **kwargs):
        self.serializer_class = SchedulerRequestSerializer
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        self.serializer_class = SchedulerResponseSerializer
        return self.create(request, *args, **kwargs)
    

class SchedulerDetail(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      generics.GenericAPIView):
    
    queryset = Scheduler.objects.all()
    serializer_class = SchedulerRequestSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)