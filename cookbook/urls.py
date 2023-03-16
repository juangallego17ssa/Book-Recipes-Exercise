from django.urls import path

from cookbook.views import ListCreateCookbookView, RetrieveUpdateDeleteCookbookView


urlpatterns = [
    path('', ListCreateCookbookView.as_view()),
    path("<int:id>/", RetrieveUpdateDeleteCookbookView.as_view()),
]