from django.contrib import admin

from recipes.models import Tag, Ingredient, Recipe, IngredientRecipe

admin.site.register(Ingredient) 
admin.site.register(Tag) 
admin.site.register(Recipe) 
admin.site.register(IngredientRecipe) 

# Register your models here.
