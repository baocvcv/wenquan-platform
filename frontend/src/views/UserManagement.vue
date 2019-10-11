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
            users: []
        }
    },
    methods: {
        create_user(user) {
            console.log("Creating a new user...");
            if (user.user_type.is_student)
            {
                this.$axios
                    .post("/accounts/students", user)
                    .then(response => {
                        console.log("Successfully create a new user.");
                    })
                    .catch(error => {
                        console.log(error);
                    });
            }
            else if (user.uesr_type.is_admin)
            {
                this.$axios
                    .post("/accounts/admins", user)
                    .then(response => {
                        console.log("Successfully create a new user.");
                    })
                    .catch(error => {
                        console.log(error);
                    });
            }
            this.users.push(user);
        },
        change_user_status(user) {
            user.is_banned = !user.is_banned;
            this.$axios
                .put("accounts/users" + user.id, user)
                .catch(error => {
                    console.log(error);
                });
        },
        change_user_type(params) {
            if (params.user_type == "Student")
                params.user.user_type.is_student = true;
            else if (params.user_type == "Admin")
                params.user.user_type.is_admin = true;
            else if (params.user_type == "SuperAdmin")
                params.user.user_type.is_superadmin = true;
            this.$axios
                .put("/accounts/users/" + params.user.id, params.user)
                .catch(error => {
                    console.log(error);
                });
        }
    },
    mounted: function() {
        this.$axios
            .get('/accounts/users')
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
       if (!this.$store.state.user || this.$store.state.user.user_type.is_student)
       {
            console.log("You have no access to this page.");
            this.$router.push("/");
       }
   }
}
</script>