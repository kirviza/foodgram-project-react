from tabnanny import verbose
from django.db import models
from django.core.validators import MinValueValidator

from users.models import User



class Tag(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Тэг'
    )
    color = models.CharField(
        max_length=7,
        unique=True,
        verbose_name='Цвет тэга'
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        null=True,
        verbose_name='Слаг тэга'
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
    unit = models.CharField(
        max_length=10,
        verbose_name='Eдиницы измерения'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Ингредиент'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='автор'
    )
    name = models.CharField(
        max_length=50,
        verbose_name='Рецепт'
    )
    text = models.TextField(verbose_name='Описание')
    time = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name='Время готовки'
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Тэг рецепта'
    )
    image = models.ImageField(
        upload_to='recipes/images/',
        verbose_name='Картинка'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата публикации'
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='recipes',
        through='IngredientRecipe',
        blank=True,
        verbose_name='Состав'
    )

    class Meta:
        ordering = ['-pub_date', 'name']
        verbose_name = 'Рецепт'

    def __str__(self):
        return self.name


class IngredientRecipe(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredient_recipe',
        verbose_name='Рецепт'
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='ingredient_recipe',
        verbose_name='Ингредиент в рецепте'
    )
    amount = models.PositiveIntegerField(
        verbose_name='Количество',
    )

    class Meta:
        verbose_name = 'Ингредиент в рецепте'

    def __str__(self):
        return '{}, {}'.format(self.ingredient, self.amount)


class ShoppingCart(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Пользователь',
    )
    recipes = models.ManyToManyField(
        Recipe,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Рецепты',
    )

    class Meta:
        verbose_name = 'Список покупок'

    def __str__(self):
        return f'{self.user}'