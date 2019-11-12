"""Url config for django rest framework"""
# from django.urls import include
from django.urls import path
# from rest_framework import routers
from rest_framework.authtoken import views as auth_views
from backend import views

# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    # auth
    path(r'api/jwt-auth/', views.auth_views.CustomAuthToken.as_view(), name='account-auth'),
    path(r'jwt-auth2/', auth_views.obtain_auth_token),
    # users
    path(r'api/accounts/users/', views.UserList.as_view(), name='user-list'),
    path(r'api/accounts/users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path(r'api/verification/', views.EmailVerificationView.as_view(), name='verification'),
    path(r'api/password/', views.ChangePasswordView.as_view(), name='password'),
    # questions
    path(r'api/questions/', views.QuestionList.as_view(), name='questions_list',),
    path(r'api/questions/<int:q_id>/', views.QuestionDetail.as_view(), name='questions_detail',),
    path(r'api/nodes_list/<int:root_id>/', views.KnowledgeNodeList.as_view(), name='nodes_list',),
    path(r'api/knowledge_nodes/<int:root_id>/', views.KnowledgeNodeDetail.as_view(), name='node_detail',),
    path(r'api/nodes_question/', views.NodeQuestionView.as_view(), name='nodes_question',),
    path(r'api/question_banks/', views.QuestionBankList.as_view(), name='banks_list',),
    path(r'api/question_banks/<int:bank_id>/', views.QuestionBankDetail.as_view(), name='banks_list',),
    path(r'api/papers/', views.PaperList.as_view(), name='papers_list',),
    path(r'api/papers/<int:paper_id>/', views.PaperDetail.as_view(), name='paper_detail',),
    path(r'api/paper_sections/<int:section_id>/', views.SectionDetail.as_view(), name='section_detail',),
    # records
    path(r'api/question_records/', views.QuestionRecordList.as_view(), name='question_record_list',),
    path(r'api/question_records/<int:pk>', views.QuestionRecordDetail.as_view(), name='question_record_detail',),
    # auth code
]
