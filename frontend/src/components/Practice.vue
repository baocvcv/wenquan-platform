<template>
  <v-card>
    <v-stepper v-model="step">
      <v-stepper-header>
        <v-stepper-step :complete="step > 1" step="1"
          >Choose Question Bank</v-stepper-step
        >
        <v-divider></v-divider>
        <v-stepper-step :complete="step > 2" step="2"
          >Number of Questions to Practice</v-stepper-step
        >
        <v-divider></v-divider>
        <v-stepper-step step="3">Start Practicing</v-stepper-step>
      </v-stepper-header>

      <v-stepper-items>
        <v-stepper-content step="1">
          <question-banks-list
            select
            readonly
            title="Question Banks"
            v-on:done-select="done_select_bank"
          />
        </v-stepper-content>
        <v-stepper-content step="2">
          <v-card>
            <v-card-text>
              <v-form v-model="valid">
                <v-text-field
                  v-model="question_number"
                  label="Question Number"
                  hint="Enter number of questions to practice"
                  :rules="question_number_rules"
                  outlined
                  required
                ></v-text-field>
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-btn text @click="step = 1">Previous Step</v-btn>
              <v-btn :disabled="!valid" text @click="step = 3">Next Step</v-btn>
            </v-card-actions>
          </v-card>
        </v-stepper-content>
        <v-stepper-content step="3">
          <h1>Developing</h1>
        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
  </v-card>
</template>

<script>
import QuestionBanksList from "@/components/QuestionBanksList.vue";
export default {
  name: "practice",
  props: {},
  components: {
    "question-banks-list": QuestionBanksList
  },
  data: function() {
    return {
      step: 0,
      bank_id: -1,
      question_number: "",
      valid: false,
      question_number_rules: [
        v => !!v || "Question number is required!",
        v => /[0-9]+/.test(v) || "An integer is expected!",
        v => v > 0 || "Question number cannot be under 1!"
      ]
    };
  },
  methods: {
    done_select_bank(id) {
      this.bank_id = id;
      console.log(this.bank_id);
      this.step = 2;
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
