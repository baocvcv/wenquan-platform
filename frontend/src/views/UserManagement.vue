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
            if (params.type == "Student")
                params.user.type.is_student = true;
            else if (params.type == "Admin")
                params.user.type.is_admin = true;
            else if (params.type == "SuperAdmin")
                params.user.type.is_superadmin = true;
            this.$axios
                .put("http://localhost:8000/accounts/students", params.user)
                .catch(error => {
                    console.log(error);
                });
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