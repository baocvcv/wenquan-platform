"""Url config for django rest framework"""
from django.urls import include, path
from rest_framework import routers
from backend import views

router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path(r'^api-auth/', include('rest_framework.urls')),
    path(r'^rest-auth/', include('rest_auth.urls')),
    path(r'^api/users^$', views.StudentCreate.as_view(), name='student-create'),
]
