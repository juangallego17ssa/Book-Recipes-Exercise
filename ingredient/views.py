import json

from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from ingredient.models import Ingredient
from ingredient.serializers import IngredientSerializer


# Create your views here.

class ListCreateIngredientView(ListCreateAPIView):

    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class RetrieveUpdateDeleteIngredientView(RetrieveUpdateDestroyAPIView):

    queryset = Ingredient.objects.all()
    lookup_field = 'id'
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]