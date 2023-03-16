from django.contrib.auth import get_user_model
from django.db import models

from recipe.models import Recipe


User = get_user_model()
# Create your models here.
class Cookbook(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField(null=False, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by_user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="added_cookbooks")
    favourite_by_user = models.ManyToManyField(to=User, related_name="fav_cookbooks", blank=True)
    recipes = models.ManyToManyField(to=Recipe, related_name="in_cookbooks")

    def __str__(self):
        return f'Cookbook {self.id} - {self.title}'
