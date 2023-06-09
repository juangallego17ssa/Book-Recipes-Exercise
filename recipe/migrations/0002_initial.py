# Generated by Django 4.1.7 on 2023-03-16 09:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("recipe", "0001_initial"),
        ("ingredient", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="created_by_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="added_recipes",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="recipe",
            name="favourite_by_user",
            field=models.ManyToManyField(
                blank=True, related_name="fav_recipes", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="recipe",
            name="ingredients",
            field=models.ManyToManyField(
                blank=True, related_name="in_recipes", to="ingredient.ingredient"
            ),
        ),
    ]
