from django.urls import path
from . import views


urlpatterns = [
    path('ajax-close-login-recommendation/', views.ajax_close_login_recommendation_view, name='ajax_close_login_recommendation'),
]