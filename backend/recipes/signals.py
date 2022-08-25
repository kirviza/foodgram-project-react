from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import FavoriteRecipe, ShoppingCart, User


@receiver(post_save, sender=User)
def create_favorite_recipe(sender, instance, created, **kwargs):
    if created:
        return FavoriteRecipe.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_shopping_cart(sender, instance, created, **kwargs):
    if created:
        return ShoppingCart.objects.create(user=instance)
