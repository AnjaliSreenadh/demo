# from django.contrib import admin
# from .models import GroceryItem, Dish, DishIngredient

# admin.site.register(GroceryItem)
# admin.site.register(Dish)
# admin.site.register(DishIngredient)
# class DishIngredientInline(admin.TabularInline):
#     model = DishIngredient
#     extra = 1  # Number of empty forms to show

# class DishAdmin(admin.ModelAdmin):
#     inlines = [DishIngredientInline]

# admin.site.register(Dish, DishAdmin)


from django.contrib import admin
from .models import GroceryItem, Dish, DishIngredient

# Register the GroceryItem model
admin.site.register(GroceryItem)

# Register the Dish model with the custom admin interface
class DishIngredientInline(admin.TabularInline):
    model = DishIngredient
    extra = 1  # Number of empty forms to show

class DishAdmin(admin.ModelAdmin):
    inlines = [DishIngredientInline]

# Now register Dish with the custom DishAdmin class
admin.site.register(Dish, DishAdmin)

# Register DishIngredient model (you don't need to register it with inlines here, as it's already linked to Dish)
admin.site.register(DishIngredient)
