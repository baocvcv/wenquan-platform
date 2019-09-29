<template>
  <div id="sign-up-box">
    <p>
      <label>用户名: </label>
      <input type="text" />
    </p>
    <p>
      <label>密码: </label>
      <input type="password" />
    </p>
    <p>
      <label>确认密码: </label>
      <input type="password" />
    </p>
    <p>
      <label>邮箱: </label>
      <input type="text" />
    </p>
    <p>
      <input type="checkbox" />
	  <label>我接受并同意《用户服务条款》和《隐私相关政策》</label>
    </p>
  </div>
</template>

<script>
export default {
  name: "sign-up-box",
  props: {
    a: Array
  },
  components: {
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

