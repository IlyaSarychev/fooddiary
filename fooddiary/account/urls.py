from django.urls import path
from . import views


urlpatterns = [
    path('ajax-close-login-recommendation/', views.ajax_close_login_recommendation_view, name='ajax_close_login_recommendation'),
    path('login/', views.ProfileLoginView.as_view(), name='login'),
    path('sign-up/', views.user_registration_view, name='user_registration'),
]