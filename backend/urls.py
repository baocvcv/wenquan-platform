"""Url config for django rest framework"""
# from django.urls import include
from django.urls import path
# from rest_framework import routers
from rest_framework.authtoken import views as auth_views
from backend import views

# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path(r'jwt-auth/', views.auth_views.CustomAuthToken.as_view(), name='account-auth'),
    path(r'jwt-auth2/', auth_views.obtain_auth_token),
    path(r'accounts/users/', views.UserList.as_view(), name='user-list'),
    path(r'accounts/users/<int:pk>/', views.UserDetail.as_view, name='user-detail'),
]
