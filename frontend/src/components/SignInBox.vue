<template>
  <div class="sign-in">
    <table>
      <tr>
        <td><v-text-field v-model="username" label="用户名"></v-text-field></td>
      </tr>
      <tr>
        <td><v-text-field v-model="password" label="密码" type="password"></v-text-field></td>
      </tr>
      <tr>
        <td>
          <v-btn v-on:click="click">Sign In</v-btn>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
import md5 from "js-md5";

export default {
  name: "sign-in",
  data: function() {
    return {
      username: "",
      password: ""
    };
  },
  methods: {
    click: function() {
      alert("usr:" + this.username + "\npsw(md5):" + md5(this.password));
    }
  }
};
</script>

<style>
.sign-in table {
  margin: auto;
}
</style>
