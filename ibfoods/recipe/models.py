# models.py
from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient, related_name='ingredient')
    instructions = models.TextField()
    
    def __str__(self) -> str:
        return f'{self.id} - {self.title}'
