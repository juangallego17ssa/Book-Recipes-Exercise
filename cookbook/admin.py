from django.contrib import admin

from cookbook.models import Cookbook
from ingredient.models import Ingredient
from recipe.models import Recipe
from user.models import User

# Register your models here.


admin.site.register(Cookbook)

admin.site.register(Recipe)

admin.site.register(Ingredient)
