<template>
  <test-view v-if="paper_id!=-1" :id="paper_id">
    <template v-slot:comment="{ paper_data }">
	  <paper-marking :paper_record_id="$route.params.id" :paper_data="paper_data" readonly/>
	</template>
  </test-view>
</template>

<script>
import PaperMarking from "@/components/PaperMarking.vue";
import TestView from "@/views/Test.vue";
import axios from "axios";
export default {
  name: "test-paper-marking",
  components: {
	"paper-marking": PaperMarking,
	"test-view": TestView
  },
  data: function() {
	return {
	  paper_id: -1
	};
  },
  created() {
	let id = this.$route.params.id;
	axios
	  .get("/api/paper_records/" + id, {
		headers: {
		  Authorization: "Token " + this.$store.state.user.token
		}
	  })
	  .then(response => {
		this.paper_id = response.data.paper_id;
		console.log("test-paper-marking-view");
		console.log(response);
	  })
	  .catch(error => {
		console.log(error)
	  })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
