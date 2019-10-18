""" Utils for testing """
from backend.models import UserPermissions

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
