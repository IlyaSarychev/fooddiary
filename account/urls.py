from unicodedata import name
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('ajax-close-login-recommendation/', views.ajax_close_login_recommendation_view, name='ajax_close_login_recommendation'),
    path('login/', views.ProfileLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/profile/login/'), name='logout'),
    path('sign-up/', views.user_registration_view, name='user_registration'),
    path('', views.ProfileDetailView.as_view(), name='profile'),
    path('edit/', views.edit_profile_view, name='edit_profile'),
    path('calorie-consumption-calculator/', views.calorie_consumption_calculator_view , name='calorie_consumption_calculator'),
]