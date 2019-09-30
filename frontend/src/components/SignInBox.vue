<template>
  <div class="sign-in">
    <input type="input" v-model="username" /><br />
    <input type="password" v-model="password" /><br />
    <input type="submit" v-on:click="click" value="Sign In" />
  </div>
</template>

<script>
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
      alert("fa Q");
    }
  }
};
</script>
