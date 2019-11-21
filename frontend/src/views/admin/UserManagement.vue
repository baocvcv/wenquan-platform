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
import axios from "axios";

export default {
  name: "user-management",
  components: {
    "user-table": user_table
  },
  data: function() {
    return {
      users: []
    };
  },
  methods: {
    create_user(user) {
      const headers = {
        Authorization: "Token " + this.$store.state.user.token
      };
      axios
        .post("/api/accounts/users/", user, { headers: headers })
        .then(response => {
          this.$$notify({
            type: "success",
            title: "Successfully create the user."
          });
          this.users.push(user);
        })
        .catch(error => {
          this.$notify({
            type: "error",
            title: "Failed to create the user :("
          });
        });
    },
    change_user_status(user) {
      let changed_user = user;
      changed_user.is_banned = !changed_user.is_banned;
      const headers = {
        Authorization: "Token " + this.$store.state.user.token
      };
      axios
        .put("/api/accounts/users/" + user.id + "/", changed_user, {
          headers: headers
        })
        .then(response => {
          if (changed_user.is_banned) {
            this.$notify({
              type: "success",
              title: "Successfully ban the user."
            });
          } else {
            this.$notify({
              type: "error",
              title: "Successfully enable the user."
            });
          }
          user = changed_user;
        })
        .catch(error => {
          this.$notify({
            type: "error",
            title: "Failed to operate :("
          });
        });
    },
    change_user_group(user) {
      let changed_user = user;
      if (changed_user.user_group === "Student")
        changed_user.user_group = "Admin";
      else if (changed_user.user_group === "Admin")
        changed_user.user_group = "Student";
      const headers = {
        Authorization: "Token " + this.$store.state.user.token
      };
      axios
        .put("/api/accounts/users/" + user.id + "/", user, { headers: headers })
        .then(response => {
          this.$notify({
            type: "success",
            title: "Successfully change the group",
            text:
              "Change the user from " +
              user.user_group +
              " to " +
              changed_user.user_group +
              "."
          });
          user = changed_user;
        })
        .catch(error => {
          this.$notify({
            type: "error",
            title: "Failed to change the group"
          });
        });
    }
  },
  mounted: function() {
    const headers = {
      Authorization: "Token " + this.$store.state.user.token
    };
    axios
      .get("/api/accounts/users/", { headers: headers })
      .then(response => {
        this.users = response.data;
      })
      .catch(error => {});
  }
};
</script>
