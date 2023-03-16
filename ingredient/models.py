from django.db import models


# Create your models here.


class Ingredient(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(null=False, blank=True)

    def __str__(self):
        return f'Ingredient {self.id} - {self.name}'
