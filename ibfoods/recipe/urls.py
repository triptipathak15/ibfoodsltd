from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from recipe.views import add_recipe, view_recipe, list_recipes

urlpatterns = [
    path('list_recipes', list_recipes, name='list_recipes'),
    path('<int:pk>/', view_recipe, name='view_recipe'),
    path('add_recipe/', add_recipe, name='add_recipe'),
]