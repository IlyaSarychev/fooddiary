from django.urls import path
from . import views


urlpatterns = [
    path('', views.DaysListView.as_view(), name='days_list'),
    path('add-day/', views.add_day, name='add_day'),
    path('day/<int:id>/', views.DayDetailView.as_view(), name='day_detail'),
    path('my-data/food/', views.MyFoodListView.as_view(), name='my_food_list'),
    path('my-data/food/create/', views.MyFoodCreateView.as_view(), name='my_food_create'),
]