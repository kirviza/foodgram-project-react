from django.contrib import admin

from recipes.models import Ingredient, Recipe, RecipeIngredient, Subscribe, Tag, ShoppingCart, FavoriteRecipe

admin.site.register(Ingredient) 
admin.site.register(Tag) 
admin.site.register(Recipe) 
admin.site.register(RecipeIngredient)
admin.site.register(FavoriteRecipe) 
admin.site.register(Subscribe) 
admin.site.register(ShoppingCart) 


# Register your models here.
