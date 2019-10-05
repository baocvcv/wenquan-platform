"""Url config for django rest framework"""
from django.urls import include, path
from rest_framework import routers
from backend import views

router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path(r'^jwt-auth/', views.obtain_auth_token)
    path(r'^api/students^$', views.StudentList.as_view(), name='student-list'),
    path(r'^api/students/<pk: int>', views.StudentDetail.as_view(), name='student-detail'),
]
