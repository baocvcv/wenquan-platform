"""Url config for django rest framework"""
from django.urls import path
from knox import views as knox_views
from backend import views

urlpatterns = [
    # path('', include(router.urls)),
    # auth
    path(r'api/jwt-auth/', views.LoginView.as_view(), name='account-auth'),
    path(r'api/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path(r'api/logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    # users
    path(r'api/accounts/users/', views.UserList.as_view(), name='user-list'),
    path(r'api/accounts/users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path(r'api/verification/', views.EmailVerificationView.as_view(), name='verification'),
    path(r'api/password/', views.ChangePasswordView.as_view(), name='password'),
    # questions
    path(
        r'api/questions/',
        views.QuestionList.as_view(),
        name='questions_list',
    ),
    path(
        r'api/questions/<int:q_id>/',
        views.QuestionDetail.as_view(),
        name='questions_detail',
    ),
    path(
        r'api/nodes_list/<int:root_id>/',
        views.KnowledgeNodeList.as_view(),
        name='nodes_list',
    ),
    path(
        r'api/knowledge_nodes/<int:root_id>/',
        views.KnowledgeNodeDetail.as_view(),
        name='node_detail',
    ),
    path(
        r'api/nodes_question/',
        views.NodeQuestionView.as_view(),
        name='nodes_question',
    ),
    path(
        r'api/question_banks/',
        views.QuestionBankList.as_view(),
        name='banks_list',
    ),
    path(
        r'api/question_banks/<int:bank_id>/',
        views.QuestionBankDetail.as_view(),
        name='banks_detail',
    ),
    path(
        r'api/papers/',
        views.PaperList.as_view(),
        name='papers_list',
    ),
    path(
        r'api/papers/<int:paper_id>/',
        views.PaperDetail.as_view(),
        name='papers_detail',
    ),
    path(
        r'api/paper_sections/<int:section_id>/',
        views.SectionDetail.as_view(),
        name='sections_detail',
    ),
    # records
    path(
        r'api/question_records/',
        views.QuestionRecordList.as_view(),
        name='question_record_list',
    ),
    path(
        r'api/question_records/<int:pk>',
        views.QuestionRecordDetail.as_view(),
        name='question_record_detail',
    ),
    path(
        r'api/paper_records/',
        views.PaperRecordList.as_view(),
        name="paper_record_list",
    ),
    path(
        r'api/paper_records',
        views.PaperRecordList.as_view(),
        name="paper_record_list",
    ),
    path(
        r'api/paper_records/<int:record_id>',
        views.PaperRecordDetail.as_view(),
        name="paper_record_detail",
    ),
    # auth-code
    path(
        r'api/auth_code/',
        views.AuthCodeView.as_view(),
        name="auth_code_create",
    ),
    path(
        r'api/auth_code/<str:code>',
        views.AuthCodeDetailView.as_view(),
        name="auth_code_activate",
    ),
    # file-upload
    path(
        r'api/upload/image/',
        views.ImageUploadView.as_view(),
        name="upload_image",
    )
]
