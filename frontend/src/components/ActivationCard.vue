<template>
  <div id="activation-card">
    <v-card>
      <v-card-title>
        Enter an Activation Code
      </v-card-title>
      <v-card-text>
        <p>
          Please enter the activation code below and click the button to
          activate.
        </p>
        <v-form v-model="valid" ref="form">
          <v-text-field
            v-model="code"
            v-bind:rules="[v => !!v || 'Activation Code is required.']"
          >
          </v-text-field>
          <v-row>
            <v-spacer></v-spacer>
            <v-btn outlined color="primary" @click="activate" :disabled="!valid"
              >Activate</v-btn
            >
            <v-spacer></v-spacer>
          </v-row>
        </v-form>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "activation-card",
  data: function() {
    return {
      code: null,
      valid: false
    };
  },
  methods: {
    activate() {
      const headers = {
        Authorization: "Token " + this.$store.state.user.token
      };
      axios({
        method: "get",
        url: "/api/auth_code/" + String(this.code),
        headers: headers
      })
        .then(response => {
          let msg =
            "The bank has been activated. You can now find it in 'MYBANK'.";
          this.$emit("activated", {
            status: true,
            msg: msg
          });
          axios
            .get("/api/accounts/users/" + this.$store.state.user.id + "/")
            .then(response => {
              this.$store.commit("updateUserWithKey", {
                key: "question_banks",
                value: response.data.question_banks
              })
            })
        })
        .catch(error => {
          if (error.response && error.response.status === 400) {
            let msg = "The code has expired or been used or is invalid.";
            this.$emit("activated", {
              status: false,
              msg: msg
            });
          } else {
            console.log(error);
          }
        });
    },
    reset() {
      this.$refs["form"].reset();
    }
  }
};
</script>
