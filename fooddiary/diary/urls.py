from django.urls import path
from . import views


urlpatterns = [
    path('', views.DaysListView.as_view(), name='days_list'),
    path('add-day/', views.add_day, name='add_day'),
    path('day/<int:id>/', views.DayDetailView.as_view(), name='day_detail'),
    path('my-data/food/', views.MyFoodListView.as_view(), name='my_food_list'),
    path('my-data/food/create/', views.MyFoodCreateView.as_view(), name='my_food_create'),
    path('my-data/food/delete/<int:id>/', views.delete_my_food_view, name='my_food_delete'),
    path('my-data/food/update/<pk>/', views.MyFoodUpdateView.as_view(), name='my_food_update'),
    path('create-meal/', views.create_meal_view, name='create_meal'),
    path('delete-meal/<int:day_id>/<int:meal_id>/', views.delete_meal_view, name='delete_meal'),
    path('get-meal-info/<int:meal_id>/', views.get_meal_info_view, name='get_meal_info'),
    path('update-meal/<int:meal_id>/', views.update_meal_view, name='update_meal'),
    path('add-food-to-meal/<int:meal_id>/', views.add_food_to_meal_view, name='add_food_to_meal'),
    path('delete-food-from-meal-view/<int:meal_id>/<int:meal_food_id>/', views.delete_food_from_meal_view, name='delete_food_from_meal'),
]