"""Url config for django rest framework"""
from django.urls import include, path
from rest_framework import routers
from backend import views

router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path(r'^api-auth/', include('rest_framework.urls')),
    path(r'^rest-auth/', include('rest_auth.urls')),
    path(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
    path(r'^api/students^$', views.StudentList.as_view(), name='student-list'),
    path(r'^api/students/<pk: int>', views.StudentDetail.as_view(), name='student-detail'),
]
