""" Utils for testing """
from backend.models import User
from backend.models import UserPermissions

USER_DATA = {
    'email': 'kb@goat.com',
    'username': 'Kobe',
    'password': '1234abcd',
    'user_group': 'Student',
}
PROFILE_DATA = {
    'school_name': 'PKU',
}

def create_permission(user_type="Student"):
    """ creat a UserPermission """
    if user_type == "Admin":
        res = UserPermissions(
            group_name="Admin",
            create_students=True,
            view_students=True,
            ban_students=True,
        )
    elif user_type == "SuperAdmin":
        res = UserPermissions(
            group_name="SuperAdmin",
            view_students=True,
            create_students=True,
            ban_students=True,
            create_admins=True,
            view_admins=True,
            ban_admins=True,
            change_user_group=True,
        )
    else:
        res = UserPermissions(group_name="Student")
    return res

def reset_database_permissions():
    """ create 3 permissions """
    create_permission().save() # Student
    create_permission("Admin").save()
    create_permission("SuperAdmin").save()

def activate_all_users():
    """ set users to be active """
    users = User.objects.all()
    for user in users:
        user.is_active = True
        user.save()
