<template>
  <div id="sign-up-box">
    <v-card>
      <v-layout row justify-center>
        <v-flex v-show="$vuetify.breakpoint.mdAndUp"> </v-flex>
        <v-flex md8>
          <v-card-text>
            <p
              class="text-center display-1 font-weight-bold text--primary text-uppercase pt-4"
            >
              sign up
            </p>
            <v-container>
              <v-form ref="input" v-model="valid">
                <v-text-field
                  v-model="user_name"
                  label="Username"
                  :rules="user_name_rules"
                  required
                ></v-text-field>

                <v-text-field
                  v-model="password"
                  label="Password"
                  :type="show_password ? 'text' : 'password'"
                  :append-icon="show_password ? 'mdi-eye' : 'mdi-eye-off'"
                  :rules="password_rules"
                  @click:append="show_password = !show_password"
                ></v-text-field>

                <v-text-field
                  v-model="re_pswd"
                  label="Re-enter password"
                  :type="show_password ? 'text' : 'password'"
                  :rules="re_password_rules"
                  required
                ></v-text-field>

                <v-text-field
                  v-model="email"
                  label="Email"
                  :rules="email_rules"
                  required
                ></v-text-field>

                <v-layout align="center">
                  <v-checkbox
                    v-model="accept_terms"
                    class="shrink mr-0 mt-0 pt-0"
                    small
                    color="primary"
                  ></v-checkbox>
                  <span :class="{ caption: true, 'grey--text': accept_terms }"
                    >I accept and agree to Terms of Service and Privacy
                    Statement</span
                  >
                </v-layout>

                <v-layout>
                  <v-spacer></v-spacer>
                  <v-btn
                    :disabled="!valid || !accept_terms"
                    outlined
                    color="primary"
                    class="mr-4"
                    @click="click"
                    >Submit
                  </v-btn>

                  <v-btn text class="mr-4 cancel-button" @click="reset_input"
                    >Reset</v-btn
                  >
                  <v-spacer></v-spacer>
                </v-layout>
              </v-form>
              <p class="text-center mt-4 mb-0 pb-0">
                <router-link to="/signup"
                  ><small
                    >Already have an account? Click here to sign in.</small
                  ></router-link
                >
              </p>
            </v-container>
          </v-card-text>
        </v-flex>
        <v-flex v-show="$vuetify.breakpoint.mdAndUp"> </v-flex>
      </v-layout>
    </v-card>
  </div>
</template>

<script>
//import md5 from "js-md5";
const axios = require("axios");

export default {
  name: "sign-up-box",
  data: function() {
    return {
      valid: false,
      user_name: "",
      user_name_rules: [
        v => !!v || "Username is required.",
        v =>
          (!!v && v.length <= 10) || "Username should be within 10 characters"
      ],
      password: "",
      show_password: false,
      password_rules: [
        v => !!v || "Password is required.",
        v => (!!v && v.length >= 8) || "At least 8 characters are required."
      ],
      re_pswd: "",
      re_password_rules: [
        v => v == this.password || "Does not consist with former one."
      ],
      email: "",
      email_rules: [
        v => !!v || "Email is required.",
        v => /.+@.+/.test(v) || "Email must be valid."
      ],
      accept_terms: false
    };
  },
  methods: {
    click: function() {
      let that = this; //store this in that so it can be used in callback functions of axios
      axios
        .post("/api/accounts/users/", {
          username: this.user_name,
          password: this.password,
          //password: md5(this.password),
          email: this.email
        })
        .then(function(response) {
          //handle success
          that.$notify({
            type: "success",
            title: "Successfully sign up",
            text:
              "An email has been sent to your mailbox. Please click the link to activate your account."
          });
          that.$router.push("/");
        })
        .catch(function(error) {
          //handle error
          that.$notify({
            type: "error",
            title: "Failed to sign up"
          });
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
a {
  color: grey;
}
a:hover {
  color: dodgerblue;
}
</style>
