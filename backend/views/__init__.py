"""import all views here to make views package"""

from .users_views import UserList
from .users_views import UserDetail
from .login_view import LoginView
from .verification_views import EmailVerificationView
from .change_password_view import ChangePasswordView

from .question_views import QuestionList
from .question_views import QuestionDetail
from .knowledge_node_views import KnowledgeNodeList
from .knowledge_node_views import KnowledgeNodeDetail
from .knowledge_node_views import NodeQuestionView
from .question_bank_views import QuestionBankList
from .question_bank_views import QuestionBankDetail
from .paper_views import PaperList
from .paper_views import PaperDetail
from .paper_views import SectionDetail

from .question_record_view import QuestionRecordList
from .question_record_view import QuestionRecordDetail
from .paper_record_views import PaperRecordList
from .paper_record_views import PaperRecordDetail

from .auth_code_views import AuthCodeView
from .auth_code_views import AuthCodeDetailView
