from django.shortcuts import render
from rest_framework import generics
from apps.users.serializers import UserSerializers, UserCreateSerializers, UserUpdateSerializers
from apps.users.models import User

# Create your views here.
class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializers

class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializers

class UserDeleteAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers