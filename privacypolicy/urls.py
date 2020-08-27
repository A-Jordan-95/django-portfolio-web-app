from django.urls import path
from . import views

urlpatterns = [
    path('', views.privacy_policy_detail, name="privacy_policy_detail"),
] 
