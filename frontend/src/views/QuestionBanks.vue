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
          <question-banks-list
            :question_banks="question_banks"
            :read_only="read_only"
          ></question-banks-list>
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
import axios from "axios";

export default {
  name: "",
  data: function() {
    return {
      read_only: false,
      question_banks: []
    };
  },
  components: {
    "question-banks-list": QuestionBanksList,
    "create-question-bank": CreateQuestionBank
  },
  methods: {
    parse(input) {
      var result = {
        id: input.id,
        name: input.name,
        brief: input.brief,
        icon: input.picture,
        details: {
          Authority: input.authority,
          "Create Time": input.createTime,
          "Last Updated Time": input.lastUpdate,
          Brief: input.brief,
          "Total Question Number": input.question_count,
          "Total Invite Code number": input.invitation_code_count,
          "Total Activated Code number": input.activated_code_count
        }
      };
      return result;
    }
  },
  created: function() {
    let that = this;
    axios
      .get("/api/question_banks/")
      .then(response => {
        for (var i = 0; i < response.data.length; i++) {
          that.question_banks.push(that.parse(response.data[i]));
        }
      })
      .catch(error => {
        alert(error);
      });
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
