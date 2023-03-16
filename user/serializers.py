
from rest_framework import serializers
from user.models import User


class UserAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'date_joined']