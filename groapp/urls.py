from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This is the homepage with the dropdown
    path('dish-list/', views.dish_list, name='dish_list'),  # This will show the ingredients for a dish

]
