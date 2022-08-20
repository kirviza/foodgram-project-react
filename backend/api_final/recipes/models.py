from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


User = get_user_model()


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
        verbose_name='Слаг тэга'
    )

    class Meta:
        ordering = ['-id']
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
        ordering = ['name']
        verbose_name = 'Ингредиент'

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipe',
        verbose_name='Автор'
    )
    name = models.CharField(
        max_length=50,
        verbose_name='Рецепт'
    )
    text = models.TextField(verbose_name='Описание')
    cooking_time = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name='Время готовки'
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Тэг рецепта'
    )
    image = models.ImageField(
        upload_to='static/images/',
        null=True,
        blank=True,
        verbose_name='Картинка'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        verbose_name='Состав'
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Рецепт'

    def __str__(self):
        return f'{self.author.email}, {self.name}'


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe',
        verbose_name='Рецепт'
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='ingredient',
        verbose_name='Ингредиент в рецепте'
    )
    amount = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        verbose_name='Количество'
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Ингредиент в рецепте'
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='unique ingredient')]


class FavoriteRecipe(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='favorite_recipe',
        verbose_name='Пользователь',
    )
    recipe = models.ManyToManyField(
        Recipe,
        related_name='favorite_recipe',
        verbose_name='Любимый рецепт',
    )

    class Meta:
        verbose_name = 'Избранное'

    def __str__(self):
        list_ = [item['name'] for item in self.recipe.values('name')]
        return f'Пользователь {self.user} добавил {list_} в избранные.'

    @receiver(post_save, sender=User)
    def create_favorite_recipe(
            sender, instance, created, **kwargs):
        if created:
            return FavoriteRecipe.objects.create(user=instance)


class Subscribe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата подписки'
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='unique_subscription')]

    def __str__(self):
        return f'Автор {self.author}, Подписчик {self.user}'


class ShoppingCart(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='shopping_cart',
        verbose_name='Пользователь'
    )

    recipe = models.ManyToManyField(
        Recipe,
        related_name='shopping_cart',
        verbose_name='Рецепты'
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Покупка'

    def __str__(self):
        list_ = [item['name'] for item in self.recipe.values('name')]
        return f'Пользователь {self.user} добавил {list_} в покупки.'

    @receiver(post_save, sender=User)
    def create_shopping_cart(
            sender, instance, created, **kwargs):
        if created:
            return ShoppingCart.objects.create(user=instance)
