from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия'
    )
    username = models.CharField(
        max_length=150,
        verbose_name='Имя пользователя'
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='Почта'
    )
    password = models.CharField(
        max_length=150,
        verbose_name='Пароль'
    )
    is_superuser = models.BooleanField(
        default=False,
        verbose_name='Администратор'
    )
    is_blocked = models.BooleanField(
        default=False,
        verbose_name='Заблокирован'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'Пользователь'

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.is_superuser


class Follow(models.Model):
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

    class Meta:
        verbose_name = 'Подписка'
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'author',),
                name='unique_follow',
            ),
        )

    def __str__(self):
        return f'{self.user} -> {self.author}'
