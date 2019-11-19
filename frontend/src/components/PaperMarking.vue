<template>
  <paper-solve v-if="paper_data && paper_record" :initData="paper_data">
    <template v-slot:shit>
	  <h1>shitttttt</h1>
	</template>
    <template v-slot:comment="{ paper }">
	  <span
	    v-for="(section, section_index) in paper.sections"
		:key="section_index"
		>
	  <question-correct
	    v-for="(question, key) in section.questions"
		:key="key"
		:question="question_info(section, question)"
	  ></question-correct>
	  </span>
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
  methods: {
	question_info(section, question) {
	  console.log("function question_info");
	  console.log(section);
	  console.log(question);
	  console.log(this.paper_record);
	  var questionRecordId = this.paper_record.questions["7"].id;
	  var result = {
		paper_record_id: this.paper_record_id,
		question_record_id: questionRecordId,
		paper_id: this.paper_record.paper_id,
		section_id: section.id,
		question_id: question.id,
		question_point: question.question_point,
		point_every_blank: question.point_every_blank
	  };
	  return result;
	}
  },
  created() {
	if (this.paper_record_id != -1) {
	  axios
		.get("/api/paper_records/" + this.paper_record_id, {
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

