from rest_framework import serializers
from ordercust.models import Customer, Order, User
from django.contrib.auth import authenticate


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'code','number']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['item', 'amount']     


class SocialAuthSerializer(serializers.Serializer):

    provider = serializers.CharField(
        max_length=30,
        allow_blank=True
    )
    access_token = serializers.CharField(
        max_length=255,
        allow_blank=True
    )
    access_token_secret = serializers.CharField(
        max_length=255,
        allow_blank=True,
        default=""
    )

    def validate(self, data):
        """Method to validate provider and access token"""
        provider = data.get('provider', None)
        access_token = data.get('access_token', None)
        access_token_secret = data.get('access_token_secret', None)
        if not provider:
            raise serializers.ValidationError(
                'A provider is required for Social Login'
            )

        if not access_token:
            raise serializers.ValidationError(
                'An access token is required for Social Login'
            )

        if provider == 'twitter' and not access_token_secret:
            raise serializers.ValidationError(
                'An access token secret is required for Twitter Login'
            )
        return data


class UserSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of User objects."""

    class Meta:
        model = User
        fields = ('email', 'username', 'token')

class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username', 'token','email','password')

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    # def validate(self, data):
        
    #     if user is None:
    #         raise serializers.ValidationError(
    #             'A user with this email and password is not found.'
    #         )
    #     try:
    #         payload = JWT_PAYLOAD_HANDLER(user)
    #         jwt_token = JWT_ENCODE_HANDLER(payload)
    #         update_last_login(None, user)
    #     except User.DoesNotExist:
    #         raise serializers.ValidationError(
    #             'User with given email and password does not exists'
    #         )
    #     return {
    #         'email':user.email,
    #         'token': jwt_token
    #     }
