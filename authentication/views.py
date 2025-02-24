
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from authentication.serializers import RegisterSerializers, LoginSerializers
from rest_framework import response, status, permissions
from django.contrib.auth import authenticate

class AuthUserAPIView(GenericAPIView):

    permission_classes=(permissions.IsAuthenticated,)

    def get(self, request):
        user=request.user

        serialiazer = RegisterSerializers(user)

        return response.Response({'user':serialiazer.data})

class RegisterAPIView(GenericAPIView):

    authentication_classes = []
    
    serializer_class=RegisterSerializers
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(GenericAPIView):
    authentication_classes = [] #for endpoints the doesnt need authentication

    serializer_class= LoginSerializers

    def post(self, request):
        email=request.data.get('email', None)
        password=request.data.get('password', None)

        user = authenticate(username=email, password=password)

        if user:
            serializer = self.serializer_class(user)
            return response.Response(serializer.data, status=status.HTTP_200_OK)

        return response.Response({'message':'Invalid credentials, try again'}, status=status.HTTP_401_UNAUTHORIZED)

