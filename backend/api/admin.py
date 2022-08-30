from django.contrib import admin

from recipes.models import (
    FavoriteRecipe, Ingredient, Recipe,
    RecipeIngredient, ShoppingCart, Subscribe, Tag
)


class IngredientAdmin(admin.ModelAdmin):
    search_fields = ('name',)


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
admin.site.register(FavoriteRecipe)
admin.site.register(Subscribe)
admin.site.register(ShoppingCart)
