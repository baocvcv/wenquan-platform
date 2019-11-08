<template>
  <div>
    <vue-element-loading :active="loading" is-full-screen></vue-element-loading>
    <test-paper :paper="paper" v-show="!loading"/> 
  </div>
</template>

<script>
import TestPaper from "@/components/TestPaper.vue";
import axios from "axios";
import VueElementLoading from "vue-element-loading";
export default {
  name: "test-paper-view",
  data: function() {
	return {
	  loading: false,
	  paper: undefined 
	};
  },
  components: {
	"test-paper": TestPaper,
	"vue-element-loading": VueElementLoading
  },
  created() {
	this.loading = true;
	let id = this.$route.params.id;
	axios
	  .get("/api/papers/" + id + "/")
	  .then(async response => {
		let result = response.data;
		console.log("first response");
		console.log(result);
		for(var i = 0; i < result.sections.length; i++) {
		  result.sections[i] = await axios.get("/api/paper_sections/" + result.sections[i].id + "/");
		  result.sections[i] = result.sections[i].data;
		  console.log("sections: "+i);
		  console.log(result.sections[i]);
		  for(var j = 0; j < result.sections[i].questions.length; j++) {
		    let question = result.sections[i].questions[j];
		    let tmp_data = await axios.get("/api/questions/" + question.id + "/");
			question["content"] = tmp_data.data;
			console.log("section: "+ i +" question: "+j);
			console.log(result.sections[i].questions[j]);
		  }
		}
		this.paper = result;
		this.loading = false;	
	  })
	  .catch(error => {
		console.log(error);
	  })
	  .then(() => {
		this.loading = false;
	  })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>

