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
    # path(r'api/auth/', include('rest_framework.urls')),
    path(r'api/signup/', views.StudentList.as_view()),
    path(r'accounts/users/', views.UserList.as_view(), name='user-list'),
    path(r'accounts/users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path(r'accounts/students/', views.StudentList.as_view(), name='student-list'),
    path(r'accounts/students/<int:pk>/', views.StudentDetail.as_view(), name='student-detail'),
    path(r'accounts/admins/', views.AdminList.as_view(), name='admin-list'),
    path(r'accounts/admins/<int:pk>/', views.AdminDetail.as_view(), name='admin-detail'),
    path(r'api/questions/', views.QuestionList.as_view(), name='questions_list'),
]
