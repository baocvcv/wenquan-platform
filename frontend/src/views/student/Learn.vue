<template>
  <v-card>
    <v-card-text>
      <v-tabs v-if="!practicing">
        <v-tab>
          <v-icon left>mdi-finance</v-icon>
          Practice
        </v-tab>
        <v-tab :disabled="practicing">
          <v-icon left>mdi-clock-outline</v-icon>
          Test
        </v-tab>
        <v-tab>
          <v-icon left>mdi-pen</v-icon>
          Records
        </v-tab>
        <v-tab-item>
          <practice v-on:practicing="start_practice" />
        </v-tab-item>
        <v-tab-item>
          <test-papers-list
            :title="
              $vuetify.breakpoint.smAndUp
                ? 'Choose a Test Paper to Simulate'
                : 'Test'
            "
            readonly
          />
        </v-tab-item>
        <v-tab-item>
          <test-paper-record-list
            :title="
              $vuetify.breakpoint.smAndUp ? 'View All Paper Records' : 'Records'
            "
          ></test-paper-record-list>
        </v-tab-item>
      </v-tabs>
      <paper-solve
        v-if="practicing"
        :initData="paper"
        @submit="finish_practicing"
      />
      <paper-marking
        v-if="view_practice_record"
        :record="practice_record"
        readonly
        :paper_data="paper"
      />
    </v-card-text>
    <vue-element-loading :active="loading" is-full-screen></vue-element-loading>
  </v-card>
</template>

<script>
import Practice from "@/components/Practice.vue";
import TestPapersList from "@/components/TestPapersList.vue";
import PaperSolve from "@/components/PaperSolve.vue";
import TestPaperRecordList from "@/components/TestPaperRecordList.vue";
import VueElementLoading from "vue-element-loading";
import PaperMarking from "@/components/PaperMarking.vue";
import axios from "axios";

export default {
  name: "learn",
  data: function() {
    return {
      practicing: false,
      paper: undefined,
      loading: false,
      practice_record: null,
      view_practice_record: false
    };
  },
  components: {
    practice: Practice,
    "test-papers-list": TestPapersList,
    "paper-solve": PaperSolve,
    "test-paper-record-list": TestPaperRecordList,
    "vue-element-loading": VueElementLoading,
    "paper-marking": PaperMarking
  },
  methods: {
    start_practice(paper) {
      this.paper = paper;
      this.practicing = true;
    },
    async finish_practicing(result) {
      this.loading = true;
      const header = {
        Authorization: "Token " + this.$store.state.user.token
      };
      let record = {
        questions: {}
      };
      for (var sec_i = 0; sec_i < result.sections.length; sec_i++)
        for (
          var qes_i = 0;
          qes_i < result.sections[sec_i].questions.length;
          qes_i++
        ) {
          let parsed_ans = {
            question_id: result.sections[sec_i].questions[qes_i].id,
            ans: result.sections[sec_i].questions[qes_i].ans
          };
          let response = await axios.post("/api/question_records", parsed_ans, {
            headers: header
          });
          let parsed_record = response.data;
          parsed_record.ans = result.sections[sec_i].questions[qes_i].ans;
          record.questions[
            parsed_record.question_id.toString()
          ] = parsed_record;
        }
      this.parsed_record = record;
      this.view_practice_record = true;
      this.loading = false;
    }
  },
  beforeRouteLeave(to, from, next) {
    if (this.practicing) {
      const answer = window.confirm(
        "Do you really want to leave? You are practicing."
      );
      if (answer) next();
      else next(false);
    } else next();
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
