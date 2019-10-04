<template>
  <div>
	<v-list two-line subheader>
	  <v-subheader inset>Question Banks</v-subheader>

	  <v-list-item
	    v-for="qst_bank in question_banks"
		:key="qst_bank.name"
		@click="redirect(qst_bank.id)"
	  >
	    <v-list-item-avatar>
		  <v-icon v-text="qst_bank.icon"
		  ></v-icon>
		</v-list-item-avatar>

		<v-list-item-content>
		  <v-list-item-title v-text="qst_bank.name"></v-list-item-title>
		  <v-list-item-subtitle v-text="qst_bank.brief"></v-list-item-subtitle>
		</v-list-item-content>

		<v-list-item-action @click="redirct('/about')">
		  <v-btn icon>
			<v-icon color="grey lighten-1">mdi-information</v-icon>
		  </v-btn>
		</v-list-item-action>
	  </v-list-item>
	</v-list>
  </div>
</template>

<script>
export default {
  name: "",
  props: {
    question_banks: {} 
  },
  data: function(){
	return {
	  
	};
  },
  methods: {
	redirct(path) {
	  this.$router.replace(path);
	}
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

