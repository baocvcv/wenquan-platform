<template>
    <div>
        <user-table
            :users="users"
            @create-user="create_user"
            @disable-user="disable_user"
            @promote-user="promote_user"
        ></user-table>
    </div>
</template>

<script>
import user_table from "@/components/UserTable.vue";

export default {
    name: "admin-index",
    components: {
        "user-table": user_table
    },
    data: function() {
        return {
            users: [
                {username: "XQ", last_login_time: "2019-09-29", ip: "192.168.0.1", type: "Admin", email: "example@example.com", disabled: false},
                {username: "XQ", last_login_time: "2019-09-29", ip: "192.168.0.1", type: "Admin", email: "example@example.com", disabled: false},
                {username: "XQ", last_login_time: "2019-09-29", ip: "192.168.0.1", type: "Admin", email: "example@example.com", disabled: false},
                {username: "XQ", last_login_time: "2019-09-29", ip: "192.168.0.1", type: "Admin", email: "example@example.com", disabled: false},
                {username: "XQ", last_login_time: "2019-09-29", ip: "192.168.0.1", type: "Admin", email: "example@example.com", disabled: false}
            ]
        }
    },
    methods: {
        create_user(user) {
            console.log("Creating a new user...");
            console.log(user);
            console.log("Successfully create a new user.");
            this.users.push(user);
        },
        disable_user(user) {
            user.disabled = !user.disabled;
        },
        promote_user(user) {

        }
    }
    /*
    mounted: function() {
        axios
            .get('api/users')
            .then(response => {
                this.users = response.data.users;
            })
            .catch(error => {
                console.log(error);
            })
    }
    */
}
</script>