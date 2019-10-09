<template>
    <div>
        <user-table
            :users="users"
            @create-user="create_user"
            @change-user-status="change_user_status"
            @change-user-type="change_user_type"
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
                {username: "XQ1", last_login_time: "2019-09-29", ip: "192.168.0.1", type: "Admin", email: "example@example.com", disabled: false},
                {username: "XQ2", last_login_time: "2019-09-29", ip: "192.168.0.1", type: "Admin", email: "example@example.com", disabled: false},
                {username: "XQ3", last_login_time: "2019-09-29", ip: "192.168.0.1", type: "Admin", email: "example@example.com", disabled: false},
                {username: "XQ4", last_login_time: "2019-09-29", ip: "192.168.0.1", type: "Admin", email: "example@example.com", disabled: false},
                {username: "XQ5", last_login_time: "2019-09-29", ip: "192.168.0.1", type: "Admin", email: "example@example.com", disabled: false}
            ]
        }
    },
    methods: {
        create_user(user) {
            console.log("Creating a new user...");
            this.$axios
                .post("http://localhost:8000/accounts/students", user)
                .then(response => {
                    console.log("Successfully create a new user.");
                })
                .catch(error => {
                    console.log(error);
                });
            this.users.push(user);
        },
        change_user_status(user) {
            user.disabled = !user.disabled;
        },
        change_user_type(params) {
            params.user.type = params.type;
        }
    },
    mounted: function() {
        this.$axios
            .get('http://localhost:8000/accounts/students')
            .then(response => {
                console.log(response);
                this.users = response.data;
                console.log(this.users);
            })
            .catch(error => {
                console.log(error);
            })
    },
   created() {
       if (!this.$store.state.user || this.$store.state.user.type != "Admin")
       {
            console.log("Failed to login as an Admin.");
            this.$router.push("/");
       }
   }
}
</script>