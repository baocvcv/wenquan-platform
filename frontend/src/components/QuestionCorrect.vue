<template>
  <question-solve>
    <template v-slot:correct="{ question_data }">
	  <v-list-item v-if="question_data.question_type != 'brief_ans'">
	  <v-spacer></v-spacer>
      <v-tooltip top>
        <template v-slot:activator="{ on }">
          <v-btn
            icon
            x-large
            @click="readonly ? () => {} : check_ans(0, question_data)"
            v-on="on"
            ><v-icon
              :color="
                correct_or_not[0] ? 'green' : 'red'
              "
              dark
              >{{
                  correct_or_not[0]
				  ? "mdi-check-circle"
                  : "mdi-close-circle"
              }}
            </v-icon></v-btn
          >
        </template>
        <span>{{ correct_or_not[0] ? 
				"Mark as wrong" : "Mark as right"
		}}</span>
      </v-tooltip>
	  <v-spacer></v-spacer>
		</v-list-item>
	  
	</template>
	<template v-slot:score="{ question_data }">
	  <v-list-item>
	    <v-text-field
		  v-model="score"
		  label="Score"
		  :readonly="readonly"
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
		  question_point: 20
		}
	  }
	}, 
	readonly: {
	  type: Boolean,
	  default: false
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
	  console.log("check");
	  if(type == "brief_ans") return score_assigned <= score_limit;
	  else return score_assigned == 0 || score_assigned == score_limit;
	},
	score_rules(question_data) {
	  return [v => /[0-9]+/.test(v) || "An integer is expected", v => this.score_overflow_check(question_data) || "Score overflow"]
	},
	check_ans(index, question_data) {
	  this.correct_or_not[index] = !this.correct_or_not[index];
	  let type = question_data.question_type;
	  if(type != "fill_blank") {
		this.score = this.correct_or_not ? this.question.question_point : 0;
	  } else {
		let point_detail = this.question.point_every_blank;
		let sum = 0;
		for(var i = 0; i < point_detail.length; i++) {
		  	sum += this.correct_or_not[i] ? point_detail[i] : 0;
		}
		this.score = sum;
	  }
	}
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>

