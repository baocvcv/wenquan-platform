<template>
    <div>
        <user-table v-bind:users="users" v-on:create-user="create_user">
        </user-table>
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
                {username: "XQ", last_login_time: "2019-09-29", ip: "192.168.0.1", type: "admin", email: "example@example.com"},
                {username: "XQ", last_login_time: "2019-09-29", ip: "192.168.0.1", type: "admin", email: "example@example.com"},
                {username: "XQ", last_login_time: "2019-09-29", ip: "192.168.0.1", type: "admin", email: "example@example.com"},
                {username: "XQ", last_login_time: "2019-09-29", ip: "192.168.0.1", type: "admin", email: "example@example.com"},
                {username: "XQ", last_login_time: "2019-09-29", ip: "192.168.0.1", type: "admin", email: "example@example.com"}
            ]
        }
    },
    methods: {
        create_user(new_user) {
            console.log("Creating a new user...");
            console.log(new_user);
            console.log("Successfully create a new user.");
            this.users.push(new_user);
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