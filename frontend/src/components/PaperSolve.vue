<template>
  <div class="paper-solve">
    <v-row>
      <v-col cols="12" lg="3" sm="4">
        <v-tabs v-model="current_section">
          <v-tab
            v-for="(item, section_index) in paper.sections"
            :key="section_index"
          >
            {{ item.title }}
          </v-tab>
          <v-tab-item
            v-for="(item, section_index) in paper.sections"
            :key="section_index"
          >
            <v-btn
              v-for="(question, index) in item.questions"
              :key="index"
              small
              icon
              outlined
              class="ma-2"
              fab
              @click="change_current_question(section_index, index)"
              :color="
                current_section == section_index && current_question == index
                  ? 'success'
                  : ''
              "
            >
              {{ index + 1 }}
            </v-btn>
          </v-tab-item>
        </v-tabs>
        <v-card>
          <v-list>
            <slot name="timer"></slot>
            <v-list-item>
              Current Question:
              {{
                paper.sections[current_section].questions[current_question]
                  .question_point
              }}
              point(s).
            </v-list-item>
            <v-list-item>
              <v-row>
                <v-btn
                  text
                  @click="previous_question"
                  :disabled="!has_previous_question"
                >
                  <v-icon left>mdi-arrow-left</v-icon>
                  Previous
                </v-btn>
                <v-spacer></v-spacer>
                <v-btn
                  text
                  @click="next_question"
                  :disabled="!has_next_question"
                >
                  Next
                  <v-icon right>mdi-arrow-right</v-icon>
                </v-btn>
              </v-row>
            </v-list-item>
            <v-list-item>
              <v-spacer></v-spacer>
			  <slot name="submit">
              <v-btn v-show="!readonly" outlined @click="submit">Submit</v-btn>
			  </slot>
              <v-spacer></v-spacer>
            </v-list-item>
          </v-list>
        </v-card>
      </v-col>
      <v-col cols="12" lg="9" sm="8">
		<slot name="comment" :paper="paper" :current_section="current_section" :current_question="current_question">
        <span
          v-for="(section, section_index) in paper.sections"
          :key="section_index"
        >
          <question-solve
            v-for="(question, question_index) in section.questions"
            :key="question_index"
            :id="question.id"
            v-show="
              current_section == section_index &&
                current_question == question_index
            "
            v-model="
              answers[current_total_index(section_index, question_index)]
            "
          ></question-solve>
        </span>
		</slot>
      </v-col>
    </v-row>
    <v-dialog v-model="warning_dialog" max-width="600px">
      <v-card>
        <v-card-title>Warning!</v-card-title>
        <v-card-text align="center">
          You have unanswered question(s). Are you sure you want to submit?
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn outlined color="error" @click="submit_confirm">Submit</v-btn>
          <v-btn outlined @click="warning_dialog = false">Cancel</v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import QuestionSolve from "@/components/QuestionSolve.vue";

export default {
  name: "paper-solve",
  components: {
    "question-solve": QuestionSolve
  },
  props: {
    initData: {
      type: Object,
      default: null
    },
	readonly: {
	  type: Boolean,
	  default: false
	}
  },
  watch: {
    initData(newVal) {
      this.paper = newVal;
    }
  },
  created() {
    if (this.initData) {
		this.paper = this.initData;
		for(var i = 0;i < this.paper.sections.length;i++){
        for(var j = 0;j < this.paper.sections[i].questions.length;j++){
          this.answers[this.current_total_index(i,j)] = [];
        }
      }
	}
  },
  data: function() {
    return {
      paper: {
        sections: []
      },
      answers: [],
      current_section: 0,
      current_question: 0,
      warning_dialog: false,
      submit_cache: null
    };
  },
  computed: {
    has_next_question() {
      return !(
        this.current_section == this.paper.sections.length - 1 &&
        this.current_question ==
          this.paper.sections[this.current_section].questions.length - 1
      );
    },
    has_previous_question() {
      return !(this.current_section == 0 && this.current_question == 0);
    },
    total_index() {
      let answer = 0;
      for (var i = 0; i < this.current_section; i++)
        answer += this.paper.sections[i].questions.length;
      answer += this.current_question;
      return answer;
    }
  },
  methods: {
    current_total_index(section, question) {
      let answer = 0;
      for (var i = 0; i < section; i++)
        answer += this.paper.sections[i].questions.length;
      answer += question;
      return answer;
    },
    change_current_question(section, question) {
      this.current_section = section;
      this.current_question = question;
    },
    next_question() {
      if (
        this.current_question <
        this.paper.sections[this.current_section].questions.length - 1
      )
        this.current_question++;
      else {
        this.current_section++;
        this.current_question = 0;
      }
    },
    previous_question() {
      if (this.current_question > 0) this.current_question--;
      else {
        this.current_section--;
        this.current_question =
          this.paper.sections[this.current_section].questions.length - 1;
      }
    },
    parse_answer(answer) {
      if(answer instanceof Array) {
	    if(answer.length == 0) return undefined;
        answer.forEach((element,index) => {
          if(!element) answer[index] = "";
        });
	  }
      return answer;
    },
    submit() {
      let result = {
        sections: []
      };
      let all_answered = true;
      for (var i = 0; i < this.paper.sections.length; i++) {
        result.sections[i] = {
          id: this.paper.sections[i].id,
          questions: []
        };
        for(var j = 0;j < this.paper.sections[i].questions.length;j++){
          let current_answer=this.parse_answer(this.answers[this.current_total_index(i,j)]);
          if(!current_answer) all_answered = false;
          result.sections[i].questions.push({
            id: this.paper.sections[i].questions[j].id,
            ans: current_answer ? current_answer : ""
          });
        }
      }
      this.submit_cache = result;
      if (!all_answered) this.warning_dialog = true;
      else this.submit_confirm();
    },
    submit_confirm() {
      if (this.submit_cache) this.$emit("submit", this.submit_cache);
    },
    force_submit() {
      let result = {
        sections: []
      };
      let all_answered = true;
      for (var i = 0; i < this.paper.sections.length; i++) {
        result.sections[i] = {
          id: this.paper.sections[i].id,
          questions: []
        };
        for(var j = 0;j < this.paper.sections[i].questions.length;j++){
          let current_answer=this.parse_answer(this.answers[this.current_total_index(i,j)]);
          if(!current_answer) all_answered = false;
          result.sections[i].questions.push({
            id: this.paper.sections[i].questions[j].id,
            ans: current_answer ? current_answer : ""
          });
        }
      }
      this.submit_cache = result;
      this.submit_confirm();
    }
  }
};
</script>
