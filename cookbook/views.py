import json

from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cookbook.models import Cookbook
from cookbook.serializers import CookbookSerializer


# Create your views here.
class ListCreateCookbookView(GenericAPIView):

    queryset = Cookbook.objects.all()
    serializer_class = CookbookSerializer
    permission_classes = [IsAuthentgizicated]

    def get(self, request):
        queryset = Cookbook.objects.all()
        serializer = CookbookSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = json.loads(request.body)
        serializer = CookbookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(CookbookSerializer(Cookbook.objects.all(), many=True).data, status=201)
        else:
            return Response(serializer.errors, status=400)


class RetrieveUpdateDeleteCookbookView(GenericAPIView):

    queryset = Cookbook.objects.all()
    lookup_field = 'id'
    serializer_class = CookbookSerializer

    def get(self, request, **kwargs):
        instance = self.get_object()
        serializer = CookbookSerializer(instance)
        return Response(serializer.data)

    def patch(self, request, **kwargs):
        instance = self.get_object()
        serializer = CookbookSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(CookbookSerializer(Cookbook.objects.all(), many=True).data)

    def delete(self, request, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(CookbookSerializer(Cookbook.objects.all(), many=True).data, status=204)


