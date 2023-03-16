from rest_framework import serializers

from recipe.serializers import RecipeSerializer
from .models import Cookbook
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CookbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cookbook
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['recipes'] = RecipeSerializer(instance.recipes, many=True).data
        representation['created_by_user'] = UserSerializer(instance.created_by_user).data
        return representation
