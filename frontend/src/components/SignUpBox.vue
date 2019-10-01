<template>
  <div id="sign-up-box">
    <v-form>
      <v-text-field
	    v-model="user_name"
		label="user name"
		required
		></v-text-field>
	  <v-text-field
	    v-model="password"
		label="password"
		type="password"
		required
	  ></v-text-field>
	  <v-text-field
	   v-model="password"
	   label="re-enter password"
	   type="password"
	   required
	  ></v-text-field>
	  <v-text-field
	    v-model="email"
		label="e-mail"
		required
	  ></v-text-field>
	  <v-checkbox
	    v-model="accept_terms"
	    label="I accept and agree to Terms of Service and Privacy Statement"
		></v-checkbox>
	  <v-btn
	    :disabled="!accept_terms"
		color="success"
		@click="click"
	  >Submit</v-btn>
	</v-form>
  </div>
</template>

<script>
export default {
  name: "sign-up-box",
  data: function() {
    return {
      user_name: "",
      password: "",
      email: "",
      accept_terms: false
    };
  },
  methods: {
    click: function() {
      alert("for test");
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#sign-up-box {
  width: 50%;
  margin: auto;
  padding: 10px;
  border: 5px dashed grey;
}
</style>
