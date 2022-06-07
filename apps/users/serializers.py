from rest_framework import serializers
from apps.users.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = "__all__"

class RegisterSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(
    #         required=True,
    #         validators=[UniqueValidator(queryset=User.objects.all())]
    #         )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Пароли отличаются"})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            # email=validated_data['email'],
            # first_name=validated_data['first_name'],
            # last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user

class UserUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = "__all__"