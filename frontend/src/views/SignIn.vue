<template>
  <div>
    <h2>Sign In</h2>
    <sign-in-box></sign-in-box>
  </div>
</template>

<script>
import SignInBox from "../components/SignInBox.vue";

export default {
  name: "sign-in",
  components: {
    "sign-in-box": SignInBox
  }
};
</script>
