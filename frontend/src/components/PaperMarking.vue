<template>
  <paper-solve :initData="paper_data">
    <template v-slot:comment="{ section }">
	  <question-correct
	    v-for="(question, key) in section.questions"
		:key="key"
		:question="question_info(section, question)"
	  ></question-correct>
	</template>
  </paper-solve>
</template>

<script>
import PaperSolve from "@/components/PaperSolve.vue";
import QuestionCorrect from "@/components/QuestionCorrect.vue";
import axios from "axios";
export default {
  name: "paper-marking",
  props: {
	paper_record_id: {
	  type: Number,
	  default: -1
	},
	paper_data: {
	  type: Object,
	  default: null,
	}
  },
  data: function() {
	return {
	  paper_record: undefined
	};
  },
  computed: {
	question_info(section, question) {
	  var questionRecordId = this.paper_record.questions[question.id].id;
	  var result = {
		paper_record_id: this.paper_record_id,
		question_record_id: questionRecordId,
		paper_id: this.paper_record.paper_id,
		section_id: section.id,
		question_id: question.id,
		question_point: 0,
		point_every_blank:[0, 0, 0]
	  };
	  return result;
	}
  },
  created() {
	if (this.paper_record_id != -1) {
	  axios
		.get("/api/paper_records/" + this.paper_record_id + "/", {
			headers: {
			  Authorization: "Token " + this.$store.state.user.token
			}
		})
	    .then(response => {
		  this.paper_record = response.data;
		  console.log("record");
		  console.log(response);
		})
		.catch(error => {
		  console.log(error);
		})
	}
  },
  components: {
	"paper-solve": PaperSolve,
	"question-correct": QuestionCorrect
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>

