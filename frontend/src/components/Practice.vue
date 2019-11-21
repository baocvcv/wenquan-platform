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
            :admin="false"
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
              <v-btn :disabled="!valid" text @click="start_practice"
                >Next Step</v-btn
              >
            </v-card-actions>
          </v-card>
        </v-stepper-content>
        <v-stepper-content step="3">
          <!--this dialog is for waiting Generating paper-->
          <v-dialog v-model="loading" hide-overlay persistent width="300">
            <v-card>
              <v-card-text>
                {{ loading_content }}
                <v-progress-circular
                  indeterminate
                  color="light-blue"
                ></v-progress-circular>
              </v-card-text>
            </v-card>
          </v-dialog>
          <span absolute center v-if="error">{{ error }}</span>
          <span absolute center v-if="warning" style="color: grey">{{
            warning
          }}</span>
        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>

    <!--dialog for warning-->
    <v-dialog v-model="warning_dialog" hide-overlay persistent width="300">
      <v-card>
        <v-card-title>Tip</v-card-title>
        <v-card-text align="center">{{ warning }}</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            text
            @click="
              warning_dialog = false;
              practing = true;
              $emit('practicing', practice_paper);
            "
            >Ok</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-card>
</template>

<script>
import QuestionBanksList from "@/components/QuestionBanksList.vue";
import axios from "axios";
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
      loading: false,
      loading_content: "Generating Practice Paper ...",
      error: "",
      warning: "",
      warning_dialog: false,
      practicing: false,
      question_number_rules: [
        v => !!v || "Question number is required!",
        v => /[0-9]+/.test(v) || "An integer is expected!",
        v => v > 0 || "Question number cannot be under 1!"
      ],
      practice_paper: undefined
    };
  },
  methods: {
    done_select_bank(id) {
      this.bank_id = id;
      this.step = 2;
    },
    start_practice() {
      this.step = 3;
      this.loading = true;
      this.error = "";
      this.warning = "";
      const headers = {
        Authorization: "Token " + this.$store.state.user.token
      };
      axios
        .get("/api/question_banks/" + this.bank_id + "/", { headers: headers })
        .then(async response => {
          let all_question = response.data.questions;

          if (all_question.length < this.question_number) {
            this.warning =
              "There are only " +
              all_question.length +
              " questions in this question banks, so we have reduced question number to the limit.";
            this.question_number = all_question.length;
          } else {
            this.warning = "Let's go! practice !";
          }

          let selected_question_id = [];
          this.practice_paper = {
            title: "Self-practice",
            total_point: this.question_num,
            sections: [
              {
                title: "Pracitice",
                total_point: this.question_num,
                section_num: "1",
                questions: []
              }
            ]
          };
          for (var i = 0; i < this.question_number; i++) {
            let rand = Math.floor(Math.random() * all_question.length);
            selected_question_id.push(all_question[rand]);
            let tmp_data = await axios.get(
              "/api/questions/" + all_question[rand] + "/",
              { headers: headers }
            );
            this.practice_paper.sections[0].questions.push({
              id: all_question[rand],
              content: tmp_data.data,
              question_point: 1,
              question_num: i + 1
            });
            all_question.splice(rand, 1);
          }
          this.warning_dialog = true;
        })
        .catch(error => {
          this.error = "Oops!" + error;
        })
        .then(() => {
          this.loading = false;
        });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
