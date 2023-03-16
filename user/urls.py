
from django.urls import path
from user.views import ListCreateUserView, RetrieveUpdateDeleteUserView


urlpatterns = [
    path('', ListCreateUserView.as_view()),
    path("<str:username>/", RetrieveUpdateDeleteUserView.as_view()),
]