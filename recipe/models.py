from django.contrib.auth import get_user_model
from django.db import models
from rest_framework.permissions import IsAuthenticated

from ingredient.models import Ingredient

User = get_user_model()


class Recipe(models.Model):

    DIFFICULTY = [
        (1, 'Easy'),
        (2, 'Intermediate'),
        (3, 'Hard'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(null=False, blank=True)
    difficulty = models.IntegerField(choices=DIFFICULTY, default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by_user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="added_recipes")
    ingredients = models.ManyToManyField(to=Ingredient, related_name="in_recipes", blank=True)
    favourite_by_user = models.ManyToManyField(to=User, related_name="fav_recipes", blank=True)

    def __str__(self):
        return f'Recipe {self.id} - {self.title}'

