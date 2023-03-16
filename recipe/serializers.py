from rest_framework import serializers
from django.contrib.auth.models import User

from ingredient.serializers import IngredientSerializer
from .models import Recipe


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class RecipeSerializer(serializers.ModelSerializer):

    # ingredients = IngredientSerializer(many=True, read_only=True)
    # created_by_user = UserSerializer(read_only=True)

    class Meta:
        model = Recipe
        # fields = ['id', 'title', 'description', 'difficulty', 'created', 'updated']
        fields = '__all__'
        extra_kwargs = {
            'created_by_user': {'read_only': True},
        }
        # depth = 1

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['ingredients'] = IngredientSerializer(instance.ingredients, many=True).data
        representation['created_by_user'] = UserSerializer(instance.created_by_user).data
        return representation
