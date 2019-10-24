"""Url config for django rest framework"""
# from django.urls import include
from django.urls import path
# from rest_framework import routers
from rest_framework.authtoken import views as auth_views
from backend import views

# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path(r'api/jwt-auth/', views.auth_views.CustomAuthToken.as_view(), name='account-auth'),
    path(r'jwt-auth2/', auth_views.obtain_auth_token),
    path(r'api/accounts/users/', views.UserList.as_view(), name='user-list'),
    path(r'api/accounts/users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path(r'api/questions/', views.QuestionList.as_view(), name='questions_list'),
    path(r'api/questions/<int:pk>/', views.QuestionDetail.as_view(), name='questions_list'),
    path(r'api/nodes_list/<int:pk>/', views.KnowledgeNodeList.as_view(), name='nodes_list'),
    path(r'api/question_banks/', views.QuestionBankList.as_view(), name='banks_list'),
    path(r'api/question_banks/<int:pk>/', views.QuestionBankDetail.as_view(), name='banks_list'),
]
