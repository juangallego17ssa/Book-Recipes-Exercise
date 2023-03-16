from django.urls import path

from recipe.views import ListCreateRecipeView, RetrieveUpdateDeleteRecipeView, LikeRecipeView

urlpatterns = [
    path('', ListCreateRecipeView.as_view()),
    path("<int:id>/", RetrieveUpdateDeleteRecipeView.as_view()),
    path("<int:id>/toogle_like/", LikeRecipeView.as_view())
]