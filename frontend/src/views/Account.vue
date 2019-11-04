<template>
<div class="account-view">
    <v-card>
        <v-card-title class="headline">
        Account
        </v-card-title>
        <v-card-text>
        <v-list>
            <v-list-item-group color="primary">
            <v-list-item>
                User Name: {{ user.username }}
            </v-list-item>
            <v-list-item>
                User Group: {{user.user_group}}
            </v-list-item>
            </v-list-item-group>
        </v-list>
        <v-btn
            outlined
            @click="password_editing = !password_editing"
            v-show="!password_editing"
        >
            Change Password
        </v-btn>
        <v-form v-model="password_valid" v-show="password_editing">
            <v-text-field
                v-model="new_psw"
                label="New password"
                type="password"
                :rules="password_rules"
                required
            ></v-text-field>
            <v-text-field
                v-model="new_psw_2"
                label="Re-enter password"
                type="password"
                :rules="re_password_rules"
                required
            ></v-text-field>
        </v-form>
        <v-btn
            outlined
            color = "success"
            @click="submit_new_psw"
            v-show="password_editing"
            class="mx-2"
        >
            Confirm
        </v-btn>
        <v-btn
            outlined
            @click="cancel_editing"
            v-show="password_editing"
            class="mx-2"
        >
            Cancel
        </v-btn>
        </v-card-text>
    </v-card>
</div>
</template>

<script>
export default {
    name: "account-view",
    computed: {
        user() {
            if(!this.$store.state.user && sessionStorage.getItem("user")){
                this.$store.commit("login", JSON.parse(sessionStorage.getItem("user")));
            }
            return this.$store.state.user;
        }
    },
    methods: {
        submit_new_psw() {
            this.password_editing = false;
            this.new_psw = "";
            this.new_psw_2 = "";
        },
        cancel_editing() {
            this.password_editing = false;
            this.new_psw = "";
            this.new_psw_2 = "";
        }
    },
    data: function() {
        return {
            password_editing: false,
            password_valid: true,
            new_psw: "",
            new_psw_2: "",
            password_rules: [
                v => !!v || "Password is required.",
                v => (!!v && v.length >= 8) || "At least 8 characters are required."
            ],
            re_password_rules: [
                v => v == this.new_psw || "Does not consist with former one."
            ],
        };
    }
};
</script>
