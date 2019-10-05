"""Url config for django rest framework"""
from django.urls import include, path
from rest_framework import routers
from backend import views

router = routers.DefaultRouter()


urlpatterns = [
    path(r'^api-auth/', include('rest_framework.urls'))
]
