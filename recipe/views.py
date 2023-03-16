import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from recipe.models import Recipe
from recipe.serializers import RecipeSerializer


# Create your views here.
class ListCreateRecipeView(GenericAPIView):

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = Recipe.objects.all()
        serializer = RecipeSerializer(queryset, many=True)
        return Response(serializer.data)
        # return JsonResponse(serializer.data, safe=False)
    # def get(self, request):
    #     recipes = Recipe.objects.all().values()
    #     return JsonResponse(list(recipes), safe=False)

    def post(self, request):
        data = json.loads(request.body)
        serializer = RecipeSerializer(data=data)
        if serializer.is_valid():
            serializer.save(created_by_user=request.user)
            return Response(RecipeSerializer(Recipe.objects.all(), many=True).data, status=201)
        else:
            return Response(serializer.errors, status=400)


class RetrieveUpdateDeleteRecipeView(GenericAPIView):

    queryset = Recipe.objects.all()
    lookup_field = 'id'
    serializer_class = RecipeSerializer

    def get(self, request, **kwargs):
        instance = self.get_object()
        serializer = RecipeSerializer(instance)
        return Response(serializer.data)

    def patch(self, request, **kwargs):
        instance = self.get_object()
        serializer = RecipeSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by_user=request.user)
        return Response(RecipeSerializer(Recipe.objects.all(), many=True).data)

    def delete(self, request, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(RecipeSerializer(Recipe.objects.all(), many=True).data, status=204)


