from django.contrib import admin
from recipe.models import Cuisine,Recipes,Review


admin.site.register(Cuisine)
admin.site.register(Recipes)

admin.site.register(Review)
