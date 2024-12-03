from django.db import models

# Create your models here.
from django.db import models

class GroceryItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock_quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(GroceryItem, through='DishIngredient')

    def __str__(self):
        return self.name

class DishIngredient(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(GroceryItem, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.dish.name} - {self.ingredient.name}"
