from django.urls import path

from ingredient.views import ListCreateIngredientView, RetrieveUpdateDeleteIngredientView


urlpatterns = [
    path('', ListCreateIngredientView.as_view()),
    path("<int:id>/", RetrieveUpdateDeleteIngredientView.as_view()),
]