# views.py
from django.shortcuts import render, redirect
from .models import Recipe, Ingredient
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from recipe.forms import RecipeForm

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


def view_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    return render(request, 'view_recipe.html', {'recipe': recipe})

def list_recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'list_recipes.html', {'rows': recipes})

# @login_required(login_url='login')
# def change_request_status(request):
#     request_ids = request.GET['leave_request_ids'].split(',')
#     new_status = request.GET['status']
#     for request_id in request_ids:
#         leave_request = LeaveRequest.objects.get(id=request_id)
#         leave_request.status = new_status
#         leave_request.save()
#     queryset = LeaveRequest.objects.all()
#     return render(request, "list_my_requests.html", {'rows': queryset})


# @login_required(login_url='login')
# def list_requests(request):
#     queryset = LeaveRequest.objects.filter(employee__employee_id=request.user.id)
#     return render(request, "list_my_requests.html", {'rows': queryset})


# @login_required(login_url='login')
# def manage_team_requests(request):
#     queryset = LeaveRequest.objects.filter(employee__manager_id=request.user.id).\
#         exclude(status="Cancelled")
#     return render(request, "manage_team_requests.html", {'rows': queryset})