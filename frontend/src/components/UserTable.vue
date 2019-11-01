<template>
  <div id="user-table">
    <v-data-table :headers="headers" :items="users" search class="elevation-1">
      <template v-slot:top>
        <v-toolbar flat color="white">
          <v-toolbar-title>User Management</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <div class="flex-grow-1"></div>
          <v-dialog v-model="dialog_create" max-width="500px">
            <template v-slot:activator="{ on }">
              <v-btn color="primary" dark class="mb-2" v-on="on"
                >New User</v-btn
              >
            </template>
            <v-card>
              <v-card-title>
                <span class="headline">New User</span>
              </v-card-title>

              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="edited_user.username"
                        label="Username"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="edited_user.password"
                        label="Password"
                        :append-icon="
                          edited_user.password_shown ? 'mdi-eye' : 'mdi-eye_off'
                        "
                        :user_type="
                          edited_user.password_shown ? 'text' : 'password'
                        "
                        @click:append="
                          edited_user.password_shown = !edited_user.password_shown
                        "
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="edited_user.email"
                        label="Email"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-select
                        v-model="edited_user.user_group"
                        label="Group"
                        :items="createable_group"
                      ></v-select>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>

              <v-card-actions>
                <div class="flex-grow-1"></div>
                <v-btn color="blue darken-1" text @click="close_dialog_create"
                  >Cancel</v-btn
                >
                <v-btn color="blue darken-1" text @click="create">Create</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>
      <template v-slot:item.user_group="{ item }">
        {{ item.user_group }}
      </template>
      <template v-slot:item.is_banned="{ item }">
        {{ item.is_banned ? "BANNED" : "NORMAL" }}
      </template>
      <template v-slot:item.action="{ item }">
        <div v-if="able_to_change_user_group(item)">
          <v-icon
            v-if="item.user_group === 'Student'"
            small
            class="mr-2"
            v-on:click="change_user_group(item)"
          >
            mdi-arrow-up
          </v-icon>
          <v-icon
            v-if="item.user_group === 'Admin'"
            small
            class="mr-2"
            v-on:click="change_user_group(item)"
          >
            mdi-arrow-down
          </v-icon>
        </div>
        <div v-if="able_to_change_user_status(item)">
          <v-icon
            v-if="item.is_banned === false"
            small
            class="mr-2"
            @click="change_user_status(item)"
          >
            mdi-cancel
          </v-icon>
          <v-icon v-else small class="mr-2" @click="change_user_status(item)">
            mdi-restore
          </v-icon>
        </div>
      </template>
    </v-data-table>
  </div>
</template>

<script>
export default {
  name: "user-table",
  components: {},
  props: {
    users: Array
  },
  data: function() {
    return {
      dialog_create: false,
      headers: [
        {
          text: "Username",
          align: "center",
          value: "username",
          sortable: false
        },
        {
          text: "Last login time",
          value: "last_login_time",
          align: "center"
        },
        {
          text: "Last login IP",
          value: "last_login_ip",
          align: "center"
        },
        {
          text: "Group",
          value: "user_group",
          align: "center"
        },
        {
          text: "Email",
          value: "email",
          align: "center",
          sortable: false
        },
        {
          text: "Status",
          value: "is_banned",
          align: "center"
        },
        {
          text: "Actions",
          value: "action",
          align: "center",
          sortable: false
        }
      ],
      edited_user: {
        username: "",
        password: "",
        email: "",
        user_group: "Student",
        password_shown: false
      },
      default_user: {
        username: "",
        password: "",
        email: "",
        user_group: "Student"
      }
    };
  },
  watch: {
    dialog(val) {
      val || this.close();
    }
  },
  computed: {
    changeable_group() {
      if (this.$store.state.user.user_permissons)
        if (this.$store.state.user.user_type.is_superadmin)
          return ["Student", "Admin", "SuperAdmin"];
        else if (this.$store.state.user.user_type.is_admin) return ["Student"];
      return [];
    },
    createable_group() {
      let group = [];
      if (this.$store.state.user.user_permissions.create_students)
        group.push("Student");
      if (this.$store.state.user.user_permissions.create_admins)
        group.push("Admin");
      return group;
    }
  },
  methods: {
    close_dialog_create() {
      this.dialog_create = false;
      setTimeout(() => {
        this.edited_user = JSON.parse(JSON.stringify(this.user));
      }, 10000);
    },
    create() {
      var new_user = {
        username: this.edited_user.username,
        password: this.edited_user.password,
        email: this.edited_user.email,
        user_group: this.edited_user.user_group,
        is_banned: false
      };
      this.$emit("create-user", new_user);
      this.close_dialog_create();
      this.edited_user = this.default_user;
    },
    change_user_group(user) {
      this.$emit("change-user-group", user);
    },
    change_user_status(user) {
      this.$emit("change-user-status", user);
    },
    able_to_change_user_group(user) {
      return this.$store.state.user.user_permissions.change_user_group;
    },
    able_to_change_user_status(user) {
      if (
        user.user_group === "Student" &&
        this.$store.state.user.user_permissions.ban_students
      )
        return true;
      if (
        user.user_group === "Admin" &&
        this.$store.state.user.user_permissions.ban_admins
      )
        return true;
      return false;
    }
  }
};
</script>
