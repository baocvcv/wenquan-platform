<template>
  <div class="sign-in">
    <table>
      <tr>
        <td>用户名：</td>
        <td><input type="input" v-model="username" /></td>
      </tr>
      <tr>
        <td>密码：</td>
        <td><input type="password" v-model="password" /></td>
      </tr>
      <tr>
        <td colspan="2">
          <input type="submit" v-on:click="click" value="Sign In" />
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
      password: "",
      userType: "Normal"
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
