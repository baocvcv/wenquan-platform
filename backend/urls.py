"""Url config for django rest framework"""
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views as auth_views
from backend import views

# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path(r'jwt-auth/', auth_views.obtain_auth_token),
    # path(r'api/auth/', include('rest_framework.urls')),
    path(r'api/students', views.UserList.as_view(), name='student-list'),
    path(r'api/students/<int:pk>', views.UserDetail.as_view(), name='student-detail'),
    path(r'accounts/students', views.StudentList.as_view(), name='student-list'),
    path(r'accounts/students/<int:pk>', views.StudentDetail.as_view(), name='student-detail'),
]
