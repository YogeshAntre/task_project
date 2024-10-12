from rest_framework import serializers
from .models import Item


class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model= Item
        fields='__all__'

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    # def create(self, validated_data):
    #     # Extract the password from validated_data
    #     password = validated_data.pop('password')
    #     # Create the user with other validated data
    #     user = User(**validated_data)
    #     # Set the password (hashed)
    #     user.set_password(password)
    #     user.save()
    #     return user