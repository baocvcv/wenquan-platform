<template>
  <div id="sign-up-box">
    <p>
      <label>用户名: </label>
      <input type="text" v-model="user_name" />
    </p>
    <p>
      <label>密码: </label>
      <input type="password" v-model="password" />
    </p>
    <p>
      <label>确认密码: </label>
      <input type="password" />
    </p>
    <p>
      <label>邮箱: </label>
      <input type="text" v-model="email" />
    </p>
    <p>
      <input type="checkbox" v-model="accept_terms" />
      <label>我接受并同意《用户服务条款》和《隐私相关政策》</label>
    </p>
    <p>
      <input type="submit" :disabled="!accept_terms" v-on:click="click" />
    </p>
  </div>
</template>

<script>
export default {
  name: "sign-up-box",
  data: function() {
    return {
      user_name: "",
      password: "",
      email: "",
      accept_terms: false
    };
  },
  methods: {
    click: function() {
      alert("shit");
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#sign-up-box {
  width: 50%;
  margin: auto;
  border: 5px dashed grey;
}
</style>
