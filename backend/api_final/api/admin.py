from django.contrib import admin

from recipes.models import (FavoriteRecipe, Ingredient, Recipe,
                            RecipeIngredient, Subscribe, ShoppingCart,
                            Tag)

admin.site.register(Ingredient)
admin.site.register(Tag)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
admin.site.register(FavoriteRecipe)
admin.site.register(Subscribe)
admin.site.register(ShoppingCart)
