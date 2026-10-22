from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.food_list_view, name='food_list'),
]