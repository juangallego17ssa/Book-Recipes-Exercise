from django.views import View
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from recipe.permissions import IsOwner
from recipe.models import Recipe
from recipe.serializers import RecipeSerializer


class ListCreateRecipeView(ListCreateAPIView):

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by_user=self.request.user)


class RetrieveUpdateDeleteRecipeView(RetrieveUpdateDestroyAPIView):

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated, IsOwner]

    def check_permissions(self, request):
        if request.method == "GET":
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]
        for permission in self.get_permissions():
            if not permission.has_permission(request, self):
                self.permission_denied(
                    request,
                    message=getattr(permission, 'message', None),
                    code=getattr(permission, 'code', None)
                )


class LikeRecipeView(View):
    def get(self, request, **kwargs):
        return
