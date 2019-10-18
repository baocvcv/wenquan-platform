<template>
    <div id="user-management">
        <user-table
            :users="users"
            @create-user="create_user"
            @change-user-status="change_user_status"
            @change-user-group="change_user_group"
        ></user-table>
    </div>
</template>

<script>
import user_table from "@/components/UserTable.vue";

export default {
    name: "user-management",
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
            this.$axios
                .post("/api/accounts/users/", user)
                .then(response => {
                    this.users.push(user);
                })
                .catch(error => {
                    console.log(error);
                })
        },
        change_user_status(user) {
            let changed_user = user;
            changed_user.is_banned = !changed_user.is_banned;
            this.$axios
                .put("/api/accounts/users/" + user.id + "/", changed_user)
                .then(response => {
                    user = changed_user;
                })
                .catch(error => {
                    console.log(error);
                });
        },
        change_user_group(user) {
            let changed_user = user;
            if (changed_user.user_group === "Student")
                changed_user.user_group = "Admin";
            else if (changed_user.user_group === "Admin")
                changed_user.user_group = "Student";
            this.$axios
                .put("/api/accounts/users/" + user.id + "/", user)
                .then(response => {
                    user = changed_user;
                })
                .catch(error => {
                    console.log(error);
                });
        }
    },
    mounted: function() {
        this.$axios
            .get('/api/accounts/users/')
            .then(response => {
                this.users = response.data;
            })
            .catch(error => {
                console.log(error);
            })
    },
   created() {
       if (!this.$store.state.user || this.$store.state.user.user_group === "Student")
       {
            console.log("You have no access to this page.");
            this.$router.push("/");
       }
       console.log(this.$store.state.user);
   }
}
</script>