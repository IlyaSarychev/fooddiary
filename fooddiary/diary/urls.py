from django.urls import path
from . import views


urlpatterns = [
    path('', views.DaysListView.as_view(), name='days_list'),
]