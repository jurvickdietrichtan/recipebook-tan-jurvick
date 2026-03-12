from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, Profile, RecipeImage


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    search_fields = ['name']
    list_display = ['name']

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ['name']
    list_display = ['name']
    inlines = [RecipeIngredientInline, RecipeImageInline]
    
class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    search_fields = ['name']
    list_display = ['name']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)

