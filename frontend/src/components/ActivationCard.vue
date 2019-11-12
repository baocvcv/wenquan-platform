<template>
  <div id="activation-card">
    <v-card>
      <v-card-title>
        Enter an Activation Code
      </v-card-title>
      <v-card-text>
        <p>
          Please enter the activation code below and click the button to
          activate.
        </p>
        <v-form v-model="valid" ref="form">
          <v-text-field
            v-model="code"
            v-bind:rules="[v => !!v || 'Activation Code is required.']"
          >
          </v-text-field>
          <v-row>
            <v-spacer></v-spacer>
            <v-btn outlined color="primary" @click="activate" :disabled="!valid"
              >Activate</v-btn
            >
            <v-spacer></v-spacer>
          </v-row>
        </v-form>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "activation-card",
  data: function() {
    return {
      code: "",
      valid: false
    };
  },
  methods: {
    activate() {},
    reset() {
      this.$refs["form"].reset();
    }
  }
};
</script>
