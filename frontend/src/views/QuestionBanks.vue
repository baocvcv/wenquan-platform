<template>
  <div>
	<h1>shit</h1>
    <question-banks-list :question_banks="question_banks"></question-banks-list>
  </div>
</template>

<script>
import QuestionBanksList from "../components/QuestionBanksList.vue";

export default {
  name: "",
  data: function() {
	return {
	  question_banks: [
	    {name: "kxz1", id: "1", icon: "mdi-folder", brief: "hahahahha"},
		{name: "kxz2", id: "2", icon: "mdi-folder", brief: "hohohoho"},
		{name: "kxz3", id: "3", icon: "mdi-folder", brief: "hehehehe"},
		{name: "kxz4", id: "4", icon: "mdi-folder", brief: "hihihihi"}
	  ]
	};
  },
  components: {
	"question-banks-list": QuestionBanksList
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
