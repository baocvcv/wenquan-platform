<template>
  <question-solve readonly>
    <template v-slot:correct="{ question_data }">
      <v-list-item
        v-if="
          question_data.question_type != 'brief_ans' &&
            question_data.question_type != 'fill_blank'
        "
      >
        <v-spacer></v-spacer>
        <v-tooltip top>
          <template v-slot:activator="{ on }">
            <v-btn
              icon
              x-large
              @click="readonly ? () => {} : check_ans(0, question_data)"
              v-on="on"
              ><v-icon :color="correct_or_not[0] ? 'green' : 'red'" dark
                >{{
                  correct_or_not[0] ? "mdi-check-circle" : "mdi-close-circle"
                }}
              </v-icon></v-btn
            >
          </template>
          <span>{{
            correct_or_not[0] ? "Mark as wrong" : "Mark as right"
          }}</span>
        </v-tooltip>
        <v-spacer></v-spacer>
      </v-list-item>
    </template>
    <template
      v-for="index in question.point_every_blank.length"
      v-slot:[slot_name(index)]="{ question_data }"
    >
      <v-tooltip :key="index" top>
        <template v-slot:activator="{ on }">
          <v-btn
            icon
            x-large
            @click="readonly ? () => {} : check_ans(index - 1, question_data)"
            v-on="on"
            ><v-icon :color="correct_or_not[index - 1] ? 'green' : 'red'" dark
              >{{
                correct_or_not[index - 1]
                  ? "mdi-check-circle"
                  : "mdi-close-circle"
              }}
            </v-icon></v-btn
          >
        </template>
        <span>{{
          correct_or_not[index - 1] ? "Mark as wrong" : "Mark as right"
        }}</span>
      </v-tooltip>
    </template>
    <template v-slot:score="{ question_data }">
      <v-list-item>
        <v-text-field
          v-model="score"
          label="Score"
          :readonly="readonly || question_data.question_type != 'brief_ans'"
          :rules="score_rules(question_data)"
          suffix="points"
          outlined
          required
        ></v-text-field>
      </v-list-item>
    </template>
    <template v-slot:comment="{ question_data }">
      <v-list-item>
        <v-textarea
          v-model="comment"
          label="Comment"
          :readonly="readonly"
          outlined
          required
        ></v-textarea>
      </v-list-item>
    </template>
  </question-solve>
</template>

<script>
import QuestionSolve from "@/components/QuestionSolve.vue";
export default {
  name: "",
  props: {
    question: {
      type: Object,
      default: () => {
        return {
          id: -1,
          question_point: 20,
          point_every_blank: [1, 2, 3]
        };
      }
    },
    readonly: {
      type: Boolean,
      default: true
    }
  },
  data: function() {
    return {
      score: 0,
      comment: "",
      correct_or_not: [false]
    };
  },
  components: {
    "question-solve": QuestionSolve
  },
  methods: {
    score_overflow_check(question_data) {
      let score_limit = this.question.question_point;
      let type = question_data.question_type;
      let score_assigned = this.score;
      return type == "brief_ans" ? score_assigned <= score_limit : true;
    },
    score_rules(question_data) {
      return [
        v => /[0-9]+/.test(v) || "An integer is expected",
        v => this.score_overflow_check(question_data) || "Score overflow"
      ];
    },
    check_ans(index, question_data) {
      this.correct_or_not[index] = !this.correct_or_not[index];
      let type = question_data.question_type;
      if (type != "fill_blank") {
        this.score = this.correct_or_not[index]
          ? this.question.question_point
          : 0;
      } else {
        let point_detail = this.question.point_every_blank;
        let sum = 0;
        for (var i = 0; i < point_detail.length; i++) {
          sum += this.correct_or_not[i] ? point_detail[i] : 0;
        }
        this.score = sum;
      }
    },
    slot_name(index) {
      return "correct-" + index.toString();
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
