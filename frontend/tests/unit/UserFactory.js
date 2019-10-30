const user_permissions = {
    "Student": {
        view_students: false,
        create_students: false,
        ban_students: false,

        view_admins: false,
        create_admins: false,
        ban_admins: false,

        change_user_group: false
    },
    "Admin": {
        view_students: true,
        create_students: true,
        ban_students: true,

        view_admins: false,
        create_admins: false,
        ban_admins: false,

        change_user_group: false
    },
    "SuperAdmin": {
        view_students: true,
        create_students: true,
        ban_students: true,

        view_admins: true,
        create_admins: true,
        ban_admins: true,

        change_user_group: true
    },
}


class UserFactory {
    constructor() {
        this.id = 0;
    }
    _create_anonymous_user() {
        let user = {
            id: this.id,
            email: "@example.org",
            username: this.id,
            password: "11111111",
            last_login_time: "2019-10-15T01:11:21.754312Z",
            last_login_ip: "127.0.0.1",
            is_banned: false,
            user_group: "",
            profile: {
                school_name: "THU",
            },
            
            // Only used when authenticating
            token: "blablabla",
        };
        this.id++;
        return user;
    }
    create_anonymous_student() {
        let user = this._create_anonymous_user();
        user.username = "Student" + user.username;
        user.email = user.username + user.email;
        user.user_group = "Student";
        user.user_permissions = user_permissions["Student"];
        return user;
    }

    create_anonymous_admin() {
        let user = this._create_anonymous_user();
        user.username = "Admin" + user.username;
        user.email = user.username + user.email;
        user.user_group = "Admin";
        user.user_permissions = user_permissions["Admin"];
        return user;
    }

    create_anonymous_superadmin() {
        let user = this._create_anonymous_user();
        user.username = "SuperAdmin" + user.username;
        user.email = user.username + user.email;
        user.user_group = "SuperAdmin";
        user.user_permissions = user_permissions["SuperAdmin"];
        return user;
    }

    log_out(wrapper) {
        sessionStorage.removeItem('user');
        wrapper.vm.$store.state.user = null;
        return wrapper;
    }

    login(wrapper, user_group) {
        if (wrapper.vm.$store.state.user)
            wrapper = this.log_out(wrapper);
        let user;
        if (user_group === "Student")
            user = this.create_anonymous_student();
        else if (user_group === "Admin")
            user = this.create_anonymous_admin();
        else if (user_group === "SuperAdmin")
            user = this.create_anonymous_superadmin();
        wrapper.vm.$store.state.user = user;
        return wrapper;
    }
};

export default UserFactory;