<template>
  <div>
    <v-card>
	  <v-toolbar flat>
	  <v-toolbar-title>{{ title }}</v-toolbar-title>
	  <v-spacer></v-spacer>
	  <v-text-field
	    flat
		hide-details
		label="Search"
		prepend-inner-icon="mdi-magnify"
		clearable
	  ></v-text-field>
	  <v-btn color="primary" elevation="0" class="ml-2" @click="create_test_paper=true">Create</v-btn>
	  </v-toolbar>
	  <v-card-text class="pt-0">
	    <p class="caption grey--text text-right mt-0 mb-0 pr-1" transition="fade-transition"
		>{{ process }}</p>
		<v-list>
		</v-list>
	  </v-card-text>
	</v-card>

	<v-dialog v-model="create_test_paper" hide-overlay fullscreen transition="dialog-bottom-transition">
	  <v-card>
	    <v-toolbar flat>
		  <v-toolbar-title>Create a Test Paper</v-toolbar-title>
		  <v-spacer></v-spacer>
		  <v-btn icon @click="create_test_paper=false">
		    <v-icon>mdi-close</v-icon>
		  </v-btn>
		</v-toolbar>
	    <test-paper create />
	  </v-card>
	</v-dialog>
  </div>
</template>

<script>
import TestPaper from "@/components/TestPaper.vue";
import axios from "axios";
export default {
  name: "test-papers-list",
  props: {
	title: {
	  type: String,
	  default: "Test Papers"
	}
  },
  components: {
	"test-paper": TestPaper
  },
  data: function() {
	return {
	  create_test_paper: false,
	  process: "",
	  test_papers: []
	};
  },
  mounted() {

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>

