<template>
  <div id="sign-up-box">
    <v-form ref="input" v-model="valid">
      <v-text-field
        v-model="user_name"
        label="user name"
        :rules="user_name_rules"
        required
      ></v-text-field>

      <v-text-field
        v-model="password"
        label="password"
        :type="show_password ? 'text' : 'password'"
        :append-icon="show_password ? 'mdi-eye' : 'mdi-eye-off'"
        :rules="password_rules"
        @click:append="show_password = !show_password"
      ></v-text-field>

      <v-text-field
        label="re-enter password"
        :type="show_password ? 'text' : 'password'"
        :rules="re_password_rules"
        required
      ></v-text-field>

      <v-text-field
        v-model="email"
        label="e-mail"
        :rules="email_rules"
        required
      ></v-text-field>

      <v-checkbox
        v-model="accept_terms"
        label="I accept and agree to Terms of Service and Privacy Statement"
      ></v-checkbox>

      <v-btn
        :disabled="!valid || !accept_terms"
        color="success"
        class="mr-4"
        @click="click"
        >Submit
      </v-btn>

      <v-btn
        color="error"
        class="mr-4"
        @click="reset_input"
        >Reset
      </v-btn>
    </v-form>
  </div>
</template>

<script>
import md5 from "js-md5";
const axios = require("axios");

export default {
  name: "sign-up-box",
  data: function() {
    return {
      valid: false,
      user_name: "",
      user_name_rules: [
        v => !!v || "user name is required",
        v => v.length <= 10 || "user name should be within 10 characters"
      ],
      password: "",
      show_password: false,
      password_rules: [
        v => !!v || "password is required",
        v => v.length >= 8 || "at least 8 characters are required"
      ],
      re_password_rules: [
        v => v == this.password || "Does not consistent with former one"
      ],
      email: "",
      email_rules: [
        v => !!v || "E-mail is required",
        v => /.+@.+/.test(v) || "E-mail must be valid"
      ],
      accept_terms: false
    };
  },
  methods: {
    click: function() {
      axios
        .post("/api/signup", {
          username: this.username,
          password: md5(this.password),
          email: this.email
        })
        .then(function(response) {
          //handle success
          alert(response.username + " successfully signed up!\nPlease sign in");
          this.$router.replace("/signin");
        })
        .catch(function(error) {
          //handle error
          alert("Sign up failed!\n" + error);
        })
        .then(function() {
          alert(this.password);
        });
    },
    reset_input() {
      this.$refs.input.reset();
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#sign-up-box {
  margin: auto;
}
</style>
