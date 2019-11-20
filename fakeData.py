""" Populate the database with fake users """
import django
import WenQuan_Platform.settings as app_settings
from django.conf import settings
from django.utils import timezone

settings.configure(INSTALLED_APPS=app_settings.INSTALLED_APPS, DATABASES=app_settings.DATABASES)
django.setup()

from backend.models import UserPermissions
from backend.models import User
from backend.models import Profile
from backend.models.question_bank import QuestionBank
from backend.models.knowledge_node import KnowledgeNode
from backend.models.questions.question_group import QuestionGroup
from backend.models.questions.choice_question import MultpChoiceQ
from backend.models.questions.brief_answer_q import BriefAnswerQ
from backend.models.questions.fill_blank_q import FillBlankQ
from backend.models.paper import Paper, Section
from backend.models.question_version import QuestionVersion


def createUser(
        username,
        password="11111111",
        email="a@b.com",
        user_group=User.STUDENT,
        is_banned=False,
):
    """ create user"""
    permission = UserPermissions.objects.get(group_name=user_group)
    profile = Profile.objects.create(school_name='THU', )
    user = User.objects.create_user(
        username=username,
        password=password,
        email=email,
        user_group=user_group,
        user_permissions=permission,
        profile=profile,
        is_banned=is_banned,
        question_banks=[],
    )
    if user_group == 'Admin':
        user.is_staff = True
    if user_group == 'SuperAdmin':
        user.is_superuser = True
    return user


createUser(username="cyx")
createUser(username="bh", is_banned=True)
createUser(username="ydf", user_group=User.ADMIN)
createUser(username='kxz', user_group=User.ADMIN)
createUser(username='xq', user_group=User.SUPER_ADMIN)


def createBank(
        name,
        picture="nothinghere",
        brief="",
        createTime=timezone.now(),
        lastUpdate=timezone.now(),
        authority="public",
        question_count=0,
        invitation_code_count=0,
        activated_code_count=0,
):
    root = KnowledgeNode.objects.create()
    root.save()
    bank = QuestionBank.objects.create(
        root_id=root.id,
        name=name,
        picture=picture,
        brief=brief,
        createTime=createTime,
        lastUpdate=lastUpdate,
        authority=authority,
        question_count=question_count,
        invitation_code_count=invitation_code_count,
        activated_code_count=activated_code_count,
    )
    bank.save()
    root.question_bank = bank
    root.save()
    return bank


multi_example = [
    {
        "question_name": "question2",
        "question_type": "multiple",
        "question_level": 5,
        "question_content": "人类的本质是?",
        "question_image": [""],
        "question_choice": ["A.复读机", "B.鸽子", "C.真香", "D.草履虫"],
        "question_ans": ["A", "B", "C"],
        "question_ans_num": 3,
        "question_solution": "某一时刻被观测时, 人类会坍缩为A,B,C中某一种情况"
    },
]

fill_blank_example = [
    {
        "question_name": "question4",
        "question_type": "fill_blank",
        "question_level": 5,
        "question_content": ["人类的本质是", "和", "还有", ""],
        "question_blank_num": 3,
        "question_image": [""],
        "question_ans": ["复读机", "鸽子", "真香"],
        "question_solution": "因为人类的本质是复读机,鸽子,真香"
    },
]

brief_q_example = [
    {
        "question_name": "question5",
        "question_type": "brief_ans",
        "question_level": 5,
        "question_content": "人类的本质是?",
        "question_image": [""],
        "question_ans": "复读机",
        "question_solution": "因为人类的本质是复读机"
    },
]

TYPEDIC = {
    'single': 1,
    'multiple': 2,
    'TorF': 3,
    'fill_blank': 4,
    'brief_ans': 5,
}

INT2TYPE = {
    '1': 'single',
    '2': 'multiple',
    '3': 'TorF',
    '4': 'fill_blank',
    '5': 'brief_ans',
}


def createQuestion(question_data, kind, bank):
    q_group = QuestionGroup.objects.create(
        current_version=timezone.now(),
        belong_bank=bank,
    )
    q_group.save()
    q_group.parents_node.set([bank.root_id])
    q_group.save()
    question_data[0]['question_change_time'] = q_group.current_version
    if kind == TYPEDIC['multiple']:
        question_data[0]['question_type'] = TYPEDIC['multiple']
        question = MultpChoiceQ.objects.create(
            **question_data[0],
            history_version=q_group,
        )
    elif kind == TYPEDIC['fill_blank']:
        question_data[0]['question_type'] = TYPEDIC['fill_blank']
        question = FillBlankQ.objects.create(
            **question_data[0],
            history_version=q_group,
        )
    else:
        question_data[0]['question_type'] = TYPEDIC['brief_ans']
        question = BriefAnswerQ.objects.create(
            **question_data[0],
            history_version=q_group,
        )
    question.save()
    return question


def createPaper(multi, fill, brief):
    paper = Paper.objects.create(
        title="test_paper",
        status="public",
        time_limit=10000,
    )
    paper.save()

    section1 = Section.objects.create(
        title="section1",
        total_point=50,
        belong_paper=paper,
        section_num=1,
    )
    section2 = Section.objects.create(
        title="section2",
        total_point=50,
        belong_paper=paper,
        section_num=2,
    )
    section1.questions.add(
        multi,
        through_defaults={
            "question_point": 50,
            "question_num": 1,
            "point_every_blank": [],
        },
    )

    section2.questions.add(
        brief,
        through_defaults={
            "question_point": 25,
            "question_num": 2,
            "point_every_blank": [],
        },
    )

    section2.questions.add(
        fill,
        through_defaults={
            "question_point": 25,
            "question_num": 3,
            "point_every_blank": [10, 10, 5],
        },
    )
    section1.save()
    section2.save()


test_bank = createBank(name="test_bank")
multi = createQuestion(multi_example, TYPEDIC['multiple'], test_bank)
fill = createQuestion(fill_blank_example, TYPEDIC['fill_blank'], test_bank)
brief = createQuestion(brief_q_example, TYPEDIC['brief_ans'], test_bank)
createPaper(multi, fill, brief)
