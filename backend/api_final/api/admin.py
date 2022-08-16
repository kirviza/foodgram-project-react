from django.contrib import admin

from recipes.models import Tag, Ingredient, Recipe, IngredientRecipe
from recipes.models import Favorite, Follow, Purchase

admin.site.register(Ingredient) 
admin.site.register(Tag) 
admin.site.register(Recipe) 
admin.site.register(IngredientRecipe)
admin.site.register(Favorite) 
admin.site.register(Follow) 
admin.site.register(Purchase) 


# Register your models here.
