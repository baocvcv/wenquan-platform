<template>
<div>
    <v-dialog v-model="dialog" max-width="500px">
        <template v-slot:activator="{ on }">
        <v-btn color="primary" dark class="mb-2" v-on="on">New User</v-btn>
        </template>
        <v-card>
        <v-card-title>
            <span class="headline">Create a new user</span>
        </v-card-title>

        <v-card-text>
            <v-container grid-list-md>
            <v-layout wrap>
                <v-flex xs12 sm6 md4>
                <v-text-field v-model="edited_user.username" label="Username"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                <v-text-field 
                    v-model="edited_user.password" 
                    label="Password"
                    :append-icon="edited_user.password_shown ? 'visibility' : 'visibility_off' "
                    :type="edited_user.password_shown ? 'text' : 'password' "
                    @click:append="edited_user.password_shown = !edited_user.password_shown"
                ></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                <v-text-field v-model="edited_user.type" label="Type"></v-text-field>
                </v-flex>
            </v-layout>
            </v-container>
        </v-card-text>

        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
            <v-btn color="blue darken-1" text @click="create">Create</v-btn>
        </v-card-actions>
        </v-card>
    </v-dialog>
    <v-data-table
    :headers="headers"
    :items="users"
    >
    <template v-slot:items="props">
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
            dialog: false,
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
                    text: "Actions",
                    value: "",
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
    methods: {
        close() {
            this.dialog = false;
            console.log(this.edited_user.username);
            setTimeout(() => {
                this.edited_user = Object.assign({}, this.default_user)
            }, 10000);
        },
        create() {
            var new_user = {
                username: this.edited_user.username,
                password: this.edited_user.password,
                type: this.edited_user.type
            };
            this.$emit("create-user", new_user);
            this.dialog = false;
        }
    }
}
</script>