<template>
  <div id="sign-up">
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12 sm8 md8>
          <sign-up-box></sign-up-box>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import SignUpBox from "../components/SignUpBox.vue";

export default {
  name: "sign-up",
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
<style scoped>
#sign-up {
  margin: 2%;
}
</style>
