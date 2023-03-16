import json

from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cookbook.models import Cookbook
from cookbook.serializers import CookbookSerializer

from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.
class ListCreateCookbookView(ListCreateAPIView):

    queryset = Cookbook.objects.all()
    serializer_class = CookbookSerializer
    permission_classes = [IsAuthenticated]


class RetrieveUpdateDeleteCookbookView(RetrieveUpdateDestroyAPIView):

    queryset = Cookbook.objects.all()
    lookup_field = 'id'
    serializer_class = CookbookSerializer

