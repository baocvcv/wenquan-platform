class UserFactory {
    constructor() {
        this.id = 0;
    }
    _create_anonymous_user() {
        let user =  {
            username: this.id,
            email: "@example.org",
            is_disabled: false,
            last_login_time: "2019-10-10",
            ip: "127.0.0.1",
            type: {
                is_student: false,
                is_admin: false,
                is_superadmin: false
            }
        };
        this.id++;
        return user;
    }
    create_anonymous_student() {
        let user = this._create_anonymous_user();
        user.username = "Student" + user.username;
        user.email = user.username + user.email;
        user.type.is_student = true;
        return user;
    }

    create_anonymous_admin() {
        let user = this._create_anonymous_user();
        user.username = "Admin" + user.username;
        user.email = user.username + user.email;
        user.type.is_admin = true;
        return user;
    }

    create_anonymous_superadmin() {
        let user = this._create_anonymous_user();
        user.username = "SuperAdmin" + user.username;
        user.email = user.username + user.email;
        user.type.is_superadmin = true;
        return user;
    }

    create_user_admin() {
        let user = this._create_anonymous_user();
        user.username = "Admin_signed_in";
        user.email = "Admin_signed_in" + user.email;
        user.type.is_admin = true;
        return user;
    }

    create_user_superadmin() {
        let user = this._create_anonymous_user();
        user.username = "SuperAdmin_signed_in" + user.email;
        user.type.is_superadmin = true;
        return user;
    }
};

export default UserFactory;