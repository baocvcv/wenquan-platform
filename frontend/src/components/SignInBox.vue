<template>
  <div class="sign-in-box">
    <v-form ref="input">
        <v-text-field
        v-model="username"
        label="用户名"
        v-bind:rules="[v => !!v || 'Username cannot be empty']"></v-text-field>
        <v-text-field
          v-model="password"
          label="密码"
          v-bind:type="show_password ? 'text' : 'password'"
          v-bind:rules="[v => !!v || 'Password cannot be empty']"
          v-bind:append-icon="show_password ? 'mdi-eye' : 'mdi-eye-off'"
          v-on:click:append="show_password=!show_password"></v-text-field>
        <v-btn v-on:click="click" v-bind:disabled="!username || !password">Sign In</v-btn>
    </v-form>
  </div>
</template>

<script>
import md5 from "js-md5";
import axios from "axios";

export default {
  name: "sign-in",
  data: function() {
    return {
      username: "",
      password: "",
      show_password: false
    };
  },
  methods: {
    click: function() {
      var cur_user=sessionStorage.getItem("user");
      if(!cur_user){
        var user = {
          username: this.username,
          password: md5(this.password)
        };
        console.log(JSON.stringify(user));
        axios.post("/jwt-auth",user).then((response) => {
          this.$store.commit("login", {
            user: user
          });
          alert(this.username+" logged in");
          this.$router.push("/");
        }).catch((response) => {
          alert(response);
        }).then(() => {

        });
      }
    }
  }
};
</script>
