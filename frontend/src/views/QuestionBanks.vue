<template>
  <div>
    <v-card>
      <v-toolbar flat color="primary" dark>
        <v-toolbar-title>Question Banks</v-toolbar-title>
      </v-toolbar>

      <v-tabs vertical>
        <v-tab align="left">
          <v-icon>mdi-book-open</v-icon>
          Browse
        </v-tab>
        <v-tab align="left">
          <v-icon>mdi-folder-plus</v-icon>
          Create
        </v-tab>

        <v-tab-item>
          <question-banks-list
            :question_banks="question_banks"
          ></question-banks-list>
        </v-tab-item>
        <v-tab-item>
          <h1>still in developing</h1>
        </v-tab-item>
      </v-tabs>
    </v-card>
  </div>
</template>

<script>
import QuestionBanksList from "../components/QuestionBanksList.vue";

export default {
  name: "",
  data: function() {
    return {
      question_banks: [
        {name: "kxz1", id: "1", icon: "mdi-library", brief: "hahahahha", details: {questions: "100", difficulty: "5", content: "this is all bullshit"}},
        {name: "kxz2", id: "2", icon: "mdi-folder", brief: "hohohoho", details: {questions: "1", difficulty: "4", content: "get out"}},
        {name: "kxz3", id: "3", icon: "mdi-folder", brief: "hehehehe"},
        {name: "kxz4", id: "4", icon: "mdi-folder", brief: "hihihihi"},
        {name: "kxz5", id: "5", icon: "mdi-folder", brief: "huhuhuhu"}
      ]
    };
  },
  components: {
    "question-banks-list": QuestionBanksList
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
