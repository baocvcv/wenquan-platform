class UserFactory {
    constructor() {
        this.id = 0;
    }
    _createAnonymousUser() {
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
    createAnonymousStudent() {
        let user = this._createAnonymousUser();
        user.username = "Student" + user.username;
        user.email = user.username + user.email;
        user.type.is_student = true;
        return user;
    }

    createAnonymousAdmin() {
        let user = this._createAnonymousUser();
        user.username = "Admin" + user.username;
        user.email = user.username + user.email;
        user.type.is_admin = true;
        return user;
    }

    createAnonymousSuperAdmin() {
        let user = this._createAnonymousUser();
        user.username = "SuperAdmin" + user.username;
        user.email = user.username + user.email;
        user.type.is_superadmin = true;
        return user;
    }
};

export default UserFactory;