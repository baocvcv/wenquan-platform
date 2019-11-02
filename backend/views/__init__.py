"""import all views here to make views package"""

from .users_views import UserList
from .users_views import UserDetail
from .auth_views import CustomAuthToken
from .verification_views import EmailVerificationView
from .change_password_view import ChangePasswordView

from .question_views import QuestionList
from .question_views import QuestionDetail
from .knowledge_node_views import KnowledgeNodeList
from .knowledge_node_views import KnowledgeNodeDetail
from .question_bank_views import QuestionBankList
from .question_bank_views import QuestionBankDetail

from .question_record_view import QuestionRecordList
from .question_record_view import QuestionRecordDetail