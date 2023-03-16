from rest_framework import serializers
from django.contrib.auth.models import User

from ingredient.serializers import IngredientSerializer
from recipe.serializers import RecipeSerializer
from .models import Cookbook


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
