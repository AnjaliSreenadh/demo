from django.shortcuts import render
from .models import Dish


def dish_list(request):
    dish_name = request.GET.get('dish_name')  # Get the selected dish name from the form
    grocery_list = []
    error_message = ''

    if dish_name:
        try:
            dish = Dish.objects.get(name=dish_name)  # Look for the dish by name
            ingredients = dish.ingredients.all()  # Get the ingredients for the dish
            
            # Build a list of ingredients with quantities
            grocery_list = [{"name": ingredient.name, 
                             "quantity": dish.dishingredient_set.get(dish=dish, ingredient=ingredient).quantity} 
                            for ingredient in ingredients]
        except Dish.DoesNotExist:
            error_message = "Dish not found."
    
    return render(request, 'shop/dish_list.html', {'grocery_list': grocery_list, 'error': error_message, 'dish_name': dish_name})

def home(request):
    # Fetch all dishes from the database
    dishes = Dish.objects.all()
    
    return render(request, 'shop/home.html', {'dishes': dishes})