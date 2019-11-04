<template>
  <div id="sign-in">
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12 sm8 md8>
          <sign-in-box></sign-in-box>
        </v-flex>
      </v-layout>
    </v-container>
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
