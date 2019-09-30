<template>
  <div id="sign-up">
    <h1>Sign up here~</h1>
    <sign-up-box></sign-up-box>
  </div>
</template>

<script>
import SignUpBox from "../components/SignUpBox.vue";

export default {
  name: "#sign-up",
  props: {},
  data: function() {
    return {
      test: "hahah"
    };
  },
  components: {
    "sign-up-box": SignUpBox
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
