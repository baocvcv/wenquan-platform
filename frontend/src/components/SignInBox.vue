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
      alert("usr:" + this.username + "\npsw(md5):" + md5(this.password));
    }
  }
};
</script>
