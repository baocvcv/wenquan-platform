<template>
  <v-card>
    <v-card-text>
      <v-tabs>
        <v-tab>
          <v-icon left>mdi-finance</v-icon>
          Practice
        </v-tab>
        <v-tab>
          <v-icon left>mdi-clock-outline</v-icon>
          Test
        </v-tab>
        <v-tab-item>
          <question-banks-list
            :flat="true"
            :readonly="true"
            select
          ></question-banks-list>
        </v-tab-item>
        <v-tab-item>
          <test-papers-list
            :title="
              $vuetify.breakpoint.smAndUp
                ? 'Choose a Test Paper to Simulate'
                : 'Test'
            "
          />
        </v-tab-item>
      </v-tabs>
    </v-card-text>
  </v-card>
</template>

<script>
import QuestionBanksList from "@/components/QuestionBanksList.vue";
import TestPapersList from "@/components/TestPapersList.vue";
export default {
  name: "learn",
  components: {
    "question-banks-list": QuestionBanksList,
    "test-papers-list": TestPapersList
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
