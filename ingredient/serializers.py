from rest_framework import serializers
from .models import Ingredient


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        # fields = ['id', 'title', 'description', 'difficulty', 'created', 'updated']
        fields = '__all__'
        # extra_kwargs = {
        #     'created_by_user': {'read_only': True},
        # }

