<template>
<div id="user-table">
    <v-dialog v-model="dialog_change_user_type" max-width="500px">
    <v-card>
    <v-card-title>
        <span class="headline">Change type to...</span>
    </v-card-title>

    <v-card-text>
        <v-container>
        <v-row>
            <v-col cols="12" sm="6" md="4">
                <v-select
                label="Type"
                v-model="selected_type"
                :items="['Student', 'Admin', 'SuperAdmin']"
                ></v-select>
            </v-col>
        </v-row>
        </v-container>
    </v-card-text>

    <v-card-actions>
        <div class="flex-grow-1"></div>
        <v-btn color="blue darken-1" text @click="close_dialog_change_user_type">Cancel</v-btn>
        <v-btn color="blue darken-1" text @click="change_user_type">Enter</v-btn>
    </v-card-actions>
    </v-card>
    </v-dialog>
    <v-data-table
    :headers="headers"
    :items="users"
    search
    class="elevation-1"
    >
    <template v-slot:top>
    <v-toolbar flat color="white">
        <v-toolbar-title>User Management</v-toolbar-title>
        <v-divider
          class="mx-4"
          inset
          vertical
        ></v-divider>
        <div class="flex-grow-1"></div>
        <v-dialog v-model="dialog_create" max-width="500px">
            <template v-slot:activator="{ on }">
                <v-btn color="primary" dark class="mb-2" v-on="on">New User</v-btn>
            </template>
            <v-card>
            <v-card-title>
                <span class="headline">New User</span>
            </v-card-title>

            <v-card-text>
                <v-container>
                <v-row>
                    <v-col cols="12" sm="6" md="4">
                    <v-text-field v-model="edited_user.username" label="Username"></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                        <v-text-field 
                            v-model="edited_user.password" 
                            label="Password"
                            :append-icon="edited_user.password_shown ? 'mdi-eye' : 'mdi-eye_off'"
                            :type="edited_user.password_shown ? 'text' : 'password' "
                            @click:append="edited_user.password_shown = !edited_user.password_shown"
                        ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                    <v-text-field v-model="edited_user.email" label="Email"></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                        <v-select
                        v-model="edited_user.type"
                        label="Type"
                        :items="['Student', 'Admin', 'SuperAdmin']"
                        ></v-select>
                    </v-col>
                </v-row>
                </v-container>
            </v-card-text>

            <v-card-actions>
                <div class="flex-grow-1"></div>
                <v-btn color="blue darken-1" text @click="close_dialog_create">Cancel</v-btn>
                <v-btn color="blue darken-1" text @click="create">Create</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:item.disabled="{ item }">
        {{ item.disabled ? "Disabled" : "Enabled" }}
    </template>
    <template v-slot:item.action="{ item }">
        <v-icon
        small
        class="mr-2"
        v-on:click="onclick(item)"
        >
        mdi-arrow-up
        </v-icon>
        <v-icon
        v-if="item.disabled === false"
        small
        class="mr-2"
        @click="disable_user(item)"
        >
        mdi-cancel
        </v-icon>
        <v-icon
        v-else
        small
        class="mr-2"
        @click="disable_user(item)"
        >
        mdi-restore
        </v-icon>
    </template>
    </v-data-table>
</div>
</template>

<script>
export default {
    name: "user-table",
    components: {
    },
    props: {
        users: Array
    },
    data: function() {
        return {
            dialog_create: false,
            dialog_change_user_type: false,
            selected_type: "",
            selected_user_index: -1,
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
                    text: "IP",
                    value: "ip",
                    align: "center"
                },
                {
                    text: "Type",
                    value: "type",
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
                    value: "disabled",
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
                type: "Student",
                password_shown: false
            },
            default_user: {
                username: "",
                password: "",
                email: "",
                type: "Student"
            },
        }   
    },
    watch: {
        dialog (val) {
            val || this.close()
        }
    },
    methods: {
        close_dialog_create() {
            this.dialog_create = false;
            setTimeout(() => {
                this.edited_user = Object.assign({}, this.default_user)
            }, 10000);
        },
        close_dialog_change_user_type() {
            this.dialog_change_user_type = false;
            this.selected_type = "";
        },
        create() {
            var new_user = {
                username: this.edited_user.username,
                password: this.edited_user.password,
                email: this.edited_user.email,
                type: this.edited_user.type,
                disabled: false
            };
            this.$emit("create-user", new_user);
            this.dialog = false;
            this.edited_user = this.default_user;
        },
        change_user_type() {
            let user = this.users[this.selected_user_index];
            if (this.selected_type == "" || this.selected_type == user.type)
                return this.close_dialog_change_user_type();
            this.dialog_change_user_type = false;
            this.$emit("change-user-type",{
                user: user,
                type: this.selected_type
            });
            this.selected_type = "";
        },
        disable_user(user) {
            this.$emit("disable-user", user);
        },
        onclick(user) {
            this.selected_user_index = this.users.indexOf(user);
            this.dialog_change_user_type = true;
        }
    }
}
</script>