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
        <v-tab align="left" :disabled="read_only">
          <v-icon>mdi-folder-plus</v-icon>
          Create
        </v-tab>

        <v-tab-item>
          <question-banks-list :read_only="read_only"></question-banks-list>
        </v-tab-item>
        <v-tab-item>
          <create-question-bank></create-question-bank>
        </v-tab-item>
      </v-tabs>
    </v-card>
  </div>
</template>

<script>
import QuestionBanksList from "../components/QuestionBanksList.vue";
import CreateQuestionBank from "../components/CreateQuestionBank.vue";

export default {
  name: "",
  data: function() {
    return {
      read_only: false
    };
  },
  components: {
    "question-banks-list": QuestionBanksList,
    "create-question-bank": CreateQuestionBank
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
