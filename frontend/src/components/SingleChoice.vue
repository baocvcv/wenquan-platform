<template>
<div>
  <v-form ref="single-choice" v-model="valid">
    <v-text-field label="Title" v-model="question_name" outlined></v-text-field>
	<v-textarea label="Content" v-model="question_content" autogrow outlined></v-textarea>
	<v-list dense>
	  <v-subheader>Choices</v-subheader>
	  <v-list-item-group color="primary">
	    <v-list-item
		  v-for="(choice,i) in question_choice"
		  :key="i">
		  <v-list-item-icon>{{ choice.name }}</v-list-item-icon>
		  <v-text-field v-model="choice.content" placeholder="Enter content"></v-text-field>
		  <v-btn icon small @click="delete_choice(i)"><v-icon dark>mdi-minus</v-icon></v-btn>
		</v-list-item>
	  </v-list-item-group>
	</v-list>
	<v-btn
	  class="mx-2"
	  fab
	  dark
	  color="indigo"
	  @click="choice_num_up()"
	>
	  <v-icon dark>mdi-plus</v-icon>
	</v-btn>
  </v-form>
</div>
</template>

<script>
export default {
  name: "",
  props: {
  },
  data:function() {
    return {
	  valid: false,
	  question_name: "",
	  question_content: "",
	  question_image: [],
	  question_choice: [],
	  question_ans: "",
	  question_solution: "",
	}	   
  },
  methods: {
    choice_num_up() {
	  let choice_num = this.question_choice.length;
	  this.question_choice.push({
		name: String.fromCharCode(choice_num + 65),
		content: ""
	  })
	},
	delete_choice(index) {
      this.question_choice.splice(index,1);
	  for(var i=0; i<this.question_choice.length; i++) {
		this.question_choice[i].name = String.fromCharCode(65 + i);
	  }
	}
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
