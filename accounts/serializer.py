from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Accounts


class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ('id', 'email', 'username', 'group_number')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ('id', 'email', 'username', 'group_number', 'password')

    def create(self, validated_data):
        user = Accounts.objects.create_user(email=validated_data['email'], username=validated_data['username'],
                                            group_number=validated_data['group_number'],
                                            password=validated_data['password'])
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials')
