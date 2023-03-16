import json

from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ingredient.models import Ingredient
from ingredient.serializers import IngredientSerializer


# Create your views here.
class ListCreateIngredientView(GenericAPIView):

    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = Ingredient.objects.all()
        serializer = IngredientSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = json.loads(request.body)
        serializer = IngredientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(IngredientSerializer(Ingredient.objects.all(), many=True).data, status=201)
        else:
            return Response(serializer.errors, status=400)


class RetrieveUpdateDeleteIngredientView(GenericAPIView):

    queryset = Ingredient.objects.all()
    lookup_field = 'id'
    serializer_class = IngredientSerializer

    def get(self, request, **kwargs):
        instance = self.get_object()
        serializer = IngredientSerializer(instance)
        return Response(serializer.data)

    def patch(self, request, **kwargs):
        instance = self.get_object()
        serializer = IngredientSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(IngredientSerializer(Ingredient.objects.all(), many=True).data)

    def delete(self, request, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(IngredientSerializer(Ingredient.objects.all(), many=True).data, status=204)


