<template>
  <div>
    <v-card>
	  <v-card-title>{{ test_paper.title }}</v-card-title>
	  <v-divider></v-divider>
	  <v-card-text>
	    <p>Total Points: {{ test_paper.total_point }}</p>
		<p>Time Limit: {{ test_paper.time_limit }}</p>
		<p>Status: {{ test_paper.status }}</p>
	  </v-card-text>

	  <v-card-actions>
	    <v-tooltip bottom>
		  <template v-slot:activator="{ on }">
			<v-btn icon v-on="on" @click="$router.push('/testpaper/' + test_paper.id)"><v-icon>mdi-goto</v-icon></v-btn>
		  </template>
		  <span>view this test paper</span>
		</v-tooltip>
		<v-tooltip bottom>
		  <template v-slot:activator="{ on }">
		    <v-btn icon v-on="on" @click="delete_test_paper = true"><v-icon>mdi-trash-can-outline</v-icon></v-btn>
		  </template>
		  <span>delete</span>
		</v-tooltip>
	  </v-card-actions>
	</v-card>

	<v-dialog v-model="delete_test_paper" max-width="300px">
	  <v-card>
	    <v-card-title>Warning</v-card-title>
		<v-divider></v-divider>
		<v-card-text align="center">
		  <span>Are you sure to delete this test paper({{ test_paper.title }})</span>
		</v-card-text>
		<v-card-actions>
		  <v-btn text @click="delete_confirmed">Confirm</v-btn>
		  <v-btn text @clic="delete_test_paper=false">Cancel</v-btn>
		</v-card-actions>
	  </v-card>
	</v-dialog>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "test-papers-list-item",
  props: {
	test_paper: {
	  type: Object,
	  default: () => {}
	}
  },
data: function() {
	return {
	  delete_test_paper: false
	};
	},
  methods: {
	delete_confirmed() {
	  axios
		.delete("/api/papers/" + this.test_paper.id + "/")
		.then(response => {
		  console.log(response);
		  this.$emit("delete");
		})
	    .catch(error => {
		  console.log(error);
		})
	}
  }  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>

