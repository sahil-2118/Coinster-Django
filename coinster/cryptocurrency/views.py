from .serializers import CryptocurrencyModelSerializer
from .models import CryptoCurrency
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import (IsAdminUser, 
                                        SAFE_METHODS,
                                        AllowAny,)



class CryptoList(APIView):

    def get(self, request):
        cryptoes   = CryptoCurrency.objects.all()
        serializer = CryptocurrencyModelSerializer(
                                                        cryptoes,
                                                        many=True,
                                                    )
        return Response(serializer.data)
    def post(self, request):
        serializer = CryptocurrencyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return (AllowAny,)
        else:
            return (IsAdminUser,)
    

class CryptoDetail(APIView):

    def get(self, request, pk):
        crypto = get_object_or_404(CryptoCurrency, pk=pk)
        serializer = CryptocurrencyModelSerializer(crypto)
        return Response(serializer.data)
    
    def put(self, request, pk):
        crypto = get_object_or_404(CryptoCurrency, pk=pk)
        serializer = CryptocurrencyModelSerializer(crypto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        crypto = get_object_or_404(CryptoCurrency, pk=pk)
        crypto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return (AllowAny,)
        else:
            return (IsAdminUser,)

