from django.shortcuts import render
from .models import FoodItem

def food_list_view(request):
    items = FoodItem.objects.all()
    return render(request, 'swiggy/food_list.html', {'items': items})