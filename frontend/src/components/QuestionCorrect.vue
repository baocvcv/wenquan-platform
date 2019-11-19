<template>
  <question-solve readonly :id="question.question_id" v-model="answer">
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
import axios from "axios";
export default {
  name: "question-correct",
  props: {
    question: {
      type: Object,
      default: () => {
        return {
		  paper_record_id: -1,
		  question_record_id: -1,
		  paper_id: -1,
		  section_id: -1,
          question_id: -1,
          question_point: 20,
          point_every_blank: [1, 2, 3],
        };
      }
    },
    readonly: {
      type: Boolean,
      default: false
    }
  },
  data: function() {
    return {
	  answer: [],
      score: 0,
      comment: "",
      correct_or_not: [false]
    };
  },
  components: {
    "question-solve": QuestionSolve
  },
  created() {
	console.log("question-correct");
	console.log(this.question);
	var record_id = this.question.question_record_id;
	if (record_id != -1) {
	  axios
		.get("/api/question_records/" + record_id, {
			headers: {
			  Authorization: "Token " + this.$store.state.user.token
			}
		})
	    .then(response => {
		  this.answer = response.data.ans;
		  this.score = response.data.score;
		  this.comment = response.data.comment;
		  var correct_bool = response.data.correct_or_not;
		  this.correct_or_not = correct_bool ? correct_bool : [response.data.is_correct];
		  console.log("question correct record got");
		  console.log(response);
		  console.log(this.answer);
		  console.log(this.correct_or_not);
		})
		.catch(error => {
		  console.log("question correct");
		  console.log(error);
		})
	} 
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
    },
	save() {
	  var marking_result = {
		paper_id: this.question.paper_id,
		section_id: this.question.section_id,
		question_id: this.question.question_id,
		comment: this.comment,
		score: this.score,
		correct_or_not: this.correct_or_not
	  }
	  axios
		.put("/api/paper_records/" + this.question.paper_record_id, marking_result)
		.then((response) => {
		  var res = {
			status: true,
			result: response
		  }
		  this.$emit("result", res);
		  console.log(response);
		})
		.catch(error => {
		  var res = {
			status: false,
			result: error
		  }
		  this.$emit("result", res);
		  console.log(error);
		})
	}
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
