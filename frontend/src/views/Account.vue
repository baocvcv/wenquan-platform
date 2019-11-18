<template>
  <div class="account-view">
    <v-card>
      <v-card-title class="headline">
        Account
      </v-card-title>
      <v-card-text>
        <v-list>
          <v-list-item-group color="primary">
            <v-list-item> User Name: {{ user.username }} </v-list-item>
            <v-list-item> User Group: {{ user.user_group }} </v-list-item>
          </v-list-item-group>
        </v-list>
        <v-btn
          outlined
          @click="password_editing = !password_editing"
          v-show="!password_editing"
        >
          Change Password
        </v-btn>
        <v-form v-model="password_valid" v-show="password_editing" ref="form">
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
          color="success"
          @click="submit_new_psw"
          v-show="password_editing"
          :disabled="!password_valid"
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
    <v-dialog v-model="dialog" max-width="600px">
      <v-card>
        <v-card-title class="headline grey lighten-2" primary-title>
          Password Edit
        </v-card-title>
        <v-card-text>
          {{ msg }}
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="
              () => {
                dialog = false;
                msg = null;
              }
            "
          >
            OK
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "account-view",
  computed: {
    user() {
      if (!this.$store.state.user && sessionStorage.getItem("user")) {
        this.$store.commit("updateUser", JSON.parse(sessionStorage.getItem("user")));
      }
      return this.$store.state.user;
    }
  },
  methods: {
    submit_new_psw() {
      axios
        .post("/api/password/", {
          token: this.user.token,
          password: this.new_psw
        })
        .then(response => {
          this.password_editing = false;
          this.msg = "Success!";
          this.dialog = true;
        })
        .catch(err => {
          this.msg = err;
          this.dialog = true;
        });
      this.$refs.form.reset();
    },
    cancel_editing() {
      this.password_editing = false;
      this.$refs.form.reset();
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
        v => (!!v && v == this.new_psw) || "Does not consist with former one."
      ],
      msg: null,
      dialog: false
    };
  }
};
</script>
