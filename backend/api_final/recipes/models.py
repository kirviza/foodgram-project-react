from tabnanny import verbose
from turtle import color
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from users.models import User



class Tag(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True
    )
    color = models.CharField(
        max_length=7,
        unique=True
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        null=True
    )

    class Meta:
        verbose_name = 'Тег'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Ингредиент'
    )
    measurement_unit = models.CharField(
        max_length=10,
        verbose_name='Eдиницы измерения'
    )

    class Meta:
        verbose_name = 'Ингредиент'

    def __str__(self):
        return self.name
