from rest_framework import serializers
from ordercust.models import Customer, Order, User


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'code']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['item', 'amount', 'time']     


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

