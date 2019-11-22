<template>
  <div>
    <vue-element-loading :active="loading" is-full-screen></vue-element-loading>
    <v-list>
      <question-correct
        v-for="(question, key) in wrong_questions"
        :key="key"
        :question="question_info(question)"
        readonly
        practice
      />
    </v-list>
  </div>
</template>

<script>
import QuestionCorrect from "@/components/QuestionCorrect.vue";
import axios from "axios";
import VueElementLoading from "vue-element-loading";
export default {
  name: "wrong-question-collection",
  components: {
    "question-correct": QuestionCorrect,
    "vue-element-loading": VueElementLoading
  },
  data: function() {
    return {
      wrong_questions: [],
      loading: false
    };
  },
  created() {
    this.loading = true;
    axios
      .get("/api/question_records/", {
        headers: {
          Authorization: "Token " + this.$store.state.user.token
        }
      })
      .then(response => {
        for (var i = 0; i < response.data.length; i++) {
          response.data[i]["point_every_blank"] = [];
          if (response.data[i].question_blank_num) {
            for (var j = 0; j < response.data[i].question_blank_num; j++) {
              response.data[i].point_every_blank.push(1);
            }
          }
        }
        this.wrong_questions = response.data;
      })
      .catch(error => {
        console.log(error);
      })
      .then(() => {
        this.loading = false;
      });
  },
  methods: {
    question_info(data) {
      var info = {
        paper_record_id: -1,
        question_record_id: data.id,
        paper_id: -1,
        section_id: -1,
        question_id: data.question_id,
        question_point: 1,
        point_every_blank: data.point_every_blank ? data.point_every_blank : []
      };
      return info;
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
