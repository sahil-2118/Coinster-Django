from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import generics
from .serializer import UserRequestSerializer, UserResponseSerializer
from .models import User
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated, AllowAny

class TokenView(ObtainAuthToken):
    pass

class ListCreateView(generics.ListCreateAPIView):

    queryset = User.objects.all()


    def get(self, request, *args, **kwargs):
        self.serializer_class = UserResponseSerializer
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        self.serializer_class = UserRequestSerializer
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        password = make_password(self.request.data['password'])
        serializer.save(password=password)

    def get_permissions(self):
        if self.request.method == 'GET':
            return (IsAuthenticated,)
        else:
            return (AllowAny,)
    

class RetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        self.serializer_class = UserResponseSerializer
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        self.serializer_class = UserRequestSerializer
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        self.serializer_class = UserRequestSerializer
        return self.delete(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        password = make_password(self.request.data['password'])
        serializer.save(password=password)
    