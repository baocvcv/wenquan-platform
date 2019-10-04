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
	    {name: "kxz1", id: "1", icon: "mdi-folder", brief: "hahahahha", details: {questions: "100", difficulty: "5", content: "this is all bullshit"}},
		{name: "kxz2", id: "2", icon: "mdi-folder", brief: "hohohoho", details: {questions: "1", difficulty: "4", content: "get out"}},
		{name: "kxz3", id: "3", icon: "mdi-folder", brief: "hehehehe"},
		{name: "kxz4", id: "4", icon: "mdi-folder", brief: "hihihihi"},
		{name: "kxz5", id: "5", icon: "mdi-folder", brief: "huhuhuhu"}
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
