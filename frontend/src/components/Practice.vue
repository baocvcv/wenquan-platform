<template>
  <v-card>
    <v-stepper v-model="step">
      <v-stepper-header>
        <v-stepper-step :complete="step > 1" step="1"
          >Choose a Question Bank</v-stepper-step
        >
        <v-divider></v-divider>
        <v-stepper-step :complete="step > 2" step="2"
          >Choose Number of Questions to Practice</v-stepper-step
        >
        <v-divider></v-divider>
        <v-stepper-step step="3">Practice</v-stepper-step>
      </v-stepper-header>
    </v-stepper>
  </v-card>
</template>

<script>
export default {
  name: "practice",
  props: {},
  components: {}
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
