# views.py
from django.shortcuts import render, redirect
from .models import Recipe, Ingredient
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from recipe.forms import RecipeForm


@login_required(login_url='login')
def add_recipe(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        ingredients = request.POST.getlist('ingredients')
        instructions = request.POST.get('instructions')
        
        recipe = Recipe.objects.create(
            title=title,
            instructions=instructions
        )
        
        for ingredient in ingredients:
            ingredient_obj, created = Ingredient.objects.get_or_create(
                name=ingredient
            )
            recipe.ingredients.add(ingredient_obj)
        
        return redirect('view_recipe', pk=recipe.pk)
    else:
        ingredients = Ingredient.objects.all()
        return render(request, 'add_recipe.html', {'ingredients': ingredients})


@login_required(login_url='login')
def view_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    return render(request, 'view_recipe.html', {'recipe': recipe})


@login_required(login_url='login')
def list_recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'list_recipes.html', {'rows': recipes})