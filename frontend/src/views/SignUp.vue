<template>
  <div id="sign-up">
    <v-card max-width="500" class="mx-auto">
      <v-toolbar color="indigo" dark>
        <v-toolbar-title>Sign up here~</v-toolbar-title>
      </v-toolbar>
      <v-card-text>
        <sign-up-box></sign-up-box>
      </v-card-text>
    </v-card>
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
