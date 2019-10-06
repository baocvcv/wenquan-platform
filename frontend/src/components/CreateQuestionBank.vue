<template>
  <div>
    <br />
    <v-card id="create-form">
      <v-toolbar color="blue" dark>
        <v-toolbar-title>Create a Question Bank</v-toolbar-title>
      </v-toolbar>
      <v-card-text>
        <v-form ref="form" v-model="valid">
          <v-text-field
            v-model="name"
            :rules="name_rules"
            hint="The name of the question bank"
            label="Name"
            outlined
            required
          ></v-text-field>
          <br />
          <v-textarea
            v-model="brief"
            :rules="brief_rules"
            hint="Brief introduction of the question bank"
            counter="200"
            label="Brief"
            auto-grow
            outlined
            required
          ></v-textarea>
          <br />
          <v-select
            :items="authorities"
            label="Authorities"
            outlined
          ></v-select>

          <v-btn color="success" :disabled="!valid" class="mr-4" @click="create"
            >Create</v-btn
          >

          <v-btn color="error" class="mr-4" @click="reset">Reset</v-btn>
        </v-form>
      </v-card-text>
    </v-card>
    <br />
  </div>
</template>

<script>
export default {
  name: "create-question-bank",
  data: function() {
    return {
      valid: false,
      name: "",
      name_rules: [
        v => !!v || "name is required!",
        v => v.length <= 200 || "Max 200 characters!"
      ],
      brief: "",
      brief_rules: [
        v => !!v || "brief introduction is required",
        v => v.length <= 200 || "Max 200 characters!"
      ],
      authorities: ["private", "public"]
    };
  },
  methods: {
    create() {
      alert("test send to backend");
    },
    reset() {
      this.$refs.form.reset();
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#create-form {
  width: 50%;
  margin: auto;
}
</style>
