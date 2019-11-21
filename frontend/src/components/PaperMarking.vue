<template>
  <div>
    <paper-solve
      v-if="paper_data && paper_record"
      :initData="paper_data"
      :readonly="readonly"
    >
      <template v-slot:comment="{ paper, current_section, current_question }">
        <span
          v-for="(section, section_index) in paper.sections"
          :key="section_index"
        >
          <question-correct
            v-for="(question, key) in section.questions"
            :key="key"
            :question="question_info(section, question)"
            ref="questions"
            v-show="current_section == section_index && current_question == key"
            :readonly="readonly"
          ></question-correct>
        </span>
      </template>
      <template v-slot:submit>
        <v-btn v-show="!readonly" outlined @click="submit">Submit</v-btn>
      </template>
    </paper-solve>
    <vue-element-loading :active="loading" is-full-screen></vue-element-loading>

    <v-dialog v-model="error" max-width="500px">
      <v-card>
        <v-card-title>Error</v-card-title>
        <v-card-text align="center">
          Please check if all scores marked are valid.
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text @click="error = false">Understand</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import PaperSolve from "@/components/PaperSolve.vue";
import QuestionCorrect from "@/components/QuestionCorrect.vue";
import VueElementLoading from "vue-element-loading";
import axios from "axios";
export default {
  name: "paper-marking",
  props: {
    paper_record_id: {
      type: Number,
      default: -1
    },
    paper_data: {
      type: Object,
      default: null
    },
    readonly: {
      type: Boolean,
      default: false
    },
    record: {
      type: Object,
      default: null
    }
  },
  data: function() {
    return {
      paper_record: undefined,
      sections: [],
      loading: false,
      error: false
    };
  },
  methods: {
    question_info(section, question) {
      console.log("function question_info");
      //console.log(section);
      console.log(question);
      //console.log(this.paper_record);
      var questionRecordId = this.paper_record.questions[question.id].id;
      var result = {
        paper_record_id: this.paper_record_id,
        question_record_id: questionRecordId,
        paper_id: this.paper_record.paper_id,
        section_id: section.id,
        question_id: question.id,
        question_point: question.question_point,
        point_every_blank: question.point_every_blank
      };
      var blank_num = question.content.question_blank_num;
      if (
        blank_num != undefined &&
        result.point_every_blank.length != blank_num
      ) {
        for (var i = 0; i < blank_num; i++) {
          result.point_every_blank.push(question.question_point / blank_num);
        }
      }
      return result;
    },
    question_ref(section_index, index) {
      if (this.sections.length <= section_index) this.sections.push([]);
      this.sections[section_index].push(index);
      return "section-" + section_index + "-question-" + index;
    },
    submit() {
      //console.log(this.$refs.questions);
      //console.log(this.$refs.questions.length);
      //console.log(this.$refs.questions[0]);
      this.loading = true;
      for (var i = 0; i < this.$refs.questions.length; i++) {
        if (
          !this.$refs.questions[i].score_form ||
          !this.$refs.questions[i].save()
        ) {
          this.error = true;
          break;
        }
      }
      this.loading = false;
      if (!this.error) this.$router.push("/admin/testpapers");
    }
  },
  created() {
    if (this.paper_record_id != -1) {
      axios
        .get("/api/paper_records/" + this.paper_record_id, {
          headers: {
            Authorization: "Token " + this.$store.state.user.token
          }
        })
        .then(response => {
          this.paper_record = response.data;
          //console.log("record");
          //console.log(response);
        })
        .catch(error => {
          console.log(error);
        });
    } else if (this.record) {
      this.paper_record = this.record;
    }
  },
  components: {
    "paper-solve": PaperSolve,
    "question-correct": QuestionCorrect,
    "vue-element-loading": VueElementLoading
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
