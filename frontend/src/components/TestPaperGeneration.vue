<template>
  <div>
    <v-form ref="input" v-model="valid">
      <v-text-field
        v-model="title"
        :rules="title_rules"
        hint="The title of the test paper"
        label="Title"
        outlined
        required
      ></v-text-field>
      <v-text-field
        v-model="total_points"
        :rules="total_points_rules"
        label="Total points"
        outlined
        required
      ></v-text-field>
      <v-textarea
        v-model="tips"
        hint="Tips provided to students(optional)"
        label="Tips"
        auto-grow
        outlined
      ></v-textarea>

      <!--list of sections-->
      <v-list>
        <v-list-item two-line>
          <v-list-item-content>
            <v-list-item-title>Sections</v-list-item-title>
            <v-list-item-subtitle :style="'color:' + section_sum_up.color">{{
              section_sum_up.content
            }}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>

        <!--sections-->
        <v-list-item-group v-for="(section, key) in edited_paper.sections" :key="key">
          <v-list-item>
            <v-list-item-avatar>
              <v-icon>{{ roman(key + 1) }}</v-icon>
            </v-list-item-avatar>
            <v-list-item-content>
              <v-row align="center">
                <v-col cols="12" xs="6" lg="4">
                  <v-text-field
                    v-model="section.title"
                    label="Title"
                    :rules="title_rules"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" xs="3" lg="2">
                  <v-text-field
                    v-model="section.total_points"
                    label="Total points"
                    :rules="total_points_rules"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" xs="3" lg="1">
                  <v-label>points</v-label>
                </v-col>
                <v-col cols="12" xs="5" lg="4">
                  <span :style="'color: ' + question_sum_up(key).color">
                    {{ question_sum_up(key).content }}
                  </span>
                </v-col>
              </v-row>
            </v-list-item-content>
            <v-list-item-action>
              <v-tooltip top>
                <template v-slot:activator="{ on }">
                  <v-btn
                    icon
                    v-on="on"
                    @click.stop="
                      adding_question = true;
                      cur_section = section;
                    "
                    ><v-icon color="green" dark>mdi-plus</v-icon>
                  </v-btn>
                </template>
                <span>Add question</span>
              </v-tooltip>
            </v-list-item-action>
            <v-list-item-action>
              <v-tooltip top>
                <template v-slot:activator="{ on }">
                  <v-btn icon v-on="on" @click.stop="drop_section(key)"
                    ><v-icon color="red" dark>mdi-trash-can-outline</v-icon>
                  </v-btn>
                </template>
                <span>remove</span>
              </v-tooltip>
            </v-list-item-action>
          </v-list-item>

          <!--questions-->
          <v-list-item-group
            v-for="(question, id) in section.questions"
            :key="id"
          >
            <!--each question-->
            <v-list-item>
              <v-list-item-avatar>{{ id + 1 + "." }}</v-list-item-avatar>
              <v-list-content>
                <v-col cols="12" xs="8" lg="6">
                  <v-text-field
                    v-model="question.point"
                    suffix="points"
                    :rules="total_points_rules"
                  ></v-text-field>
                </v-col>
              </v-list-content>
              <v-list-item-action>
                <v-tooltip top>
                  <template v-slot:activator="{ on }">
                    <v-btn icon v-on="on" @click="drop_question(section, id)"
                      ><v-icon color="red">mdi-trash-can-outline</v-icon>
                    </v-btn>
                  </template>
                  <span>Remove this question</span>
                </v-tooltip>
              </v-list-item-action>
            </v-list-item>
            <question-list-item :question="question.content" dialog="true" />
          </v-list-item-group>
        </v-list-item-group>
        <v-list-item>
          <v-list-item-content>
            <v-btn
              class="mx-2"
              block
              tile
              dark
              color="green"
              @click="create_section()"
              >Create new</v-btn
            >
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <v-btn
        color="success"
        :disabled="!valid || !judge_points_sum"
        class="mr-4"
        @click="submit()"
        >Save</v-btn
      >
      <v-btn color="error" class="mr-4" @click="reset()">Reset</v-btn>
      <v-btn :disabled="!paper" class="mr-4" @click="cancel()">Cancel</v-btn>
    </v-form>

    <!--The dialog is for selecting questions-->
    <v-dialog
      v-model="adding_question"
      fullscreen
      hide-overlay
      transition="dialog-bottom-transition"
    >
      <v-card>
        <v-toolbar>
          <v-tooltip bottom>
            <template v-slot:activator="{ on }">
              <v-btn
                v-if="process == 'question'"
                v-on="on"
                icon
                @click="process = 'question bank'"
                ><v-icon>mdi-arrow-left</v-icon>
              </v-btn>
            </template>
            <span>Back to question banks list</span>
          </v-tooltip>

          <v-tooltip bottom>
            <template v-slot:activator="{ on }">
              <v-btn v-on="on" icon @click="adding_question = false">
                <v-icon>mdi-close</v-icon>
              </v-btn>
            </template>
            <span>Close</span>
          </v-tooltip>
          <v-toolbar-title>Selecting {{ process }}</v-toolbar-title>
        </v-toolbar>
        <question-banks-list
          v-if="process == 'question bank'"
          select
          readonly
          v-on:done-select="get_bank_id"
        />
        <question-list
          v-if="process == 'question'"
          :id="question_bank_id"
          editable="true"
          dialog="true"
          select
          v-on:done-select="get_selected_questions"
          v-on:cancel-select="process = 'question bank'"
        />
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import QuestionBanksList from "@/components/QuestionBanksList.vue";
import QuestionList from "@/components/QuestionList.vue";
import QuestionListItem from "@/components/QuestionListItem.vue";
import axios from "axios";

export default {
  name: "",
  props: {
    paper: {
      type: Object,
      default: undefined
    },
    id: -1
  },
  model: {
    prop: "paper",
    event: "save"
  },
  components: {
    "question-banks-list": QuestionBanksList,
    "question-list": QuestionList,
    "question-list-item": QuestionListItem
  },
  data: function() {
    return {
      valid: false,
      edited_paper: {
        title: "",
        total_points: "0",
        tips: "",
        sections: []
      },
      title_rules: [v => !!v || "Title is required!"],
      total_points_rules: [
        v => !!v || "Total points is required!",
        v => (!!v && /^[0-9]+$/.test(v)) || "An integer is expected!"
      ],
      cur_section: undefined,
      adding_question: false,
      process: "question bank"
    };
  },
  computed: {
    section_sum_up: function() {
      //sum up of points assigned to each section and check if sum == total points of test paper
      let sum = 0;
      for (var i = 0; i < this.edited_paper.sections.length; i++) {
        sum += parseInt(this.edited_paper.sections[i].total_points);
      }
      var tip =
        sum == this.total_points && !!this.total_points
          ? { color: "green", content: "valid" }
          : {
              color: "red",
              content:
                "Sum-up of points of sections: " +
                sum +
                " | Points assigned to this test paper: " +
                this.total_points
            };
      return tip;
    },
    judge_points_sum: function() {
      if (this.section_sum_up.content != "valid") {
        console.log("section");
        console.log(this.section_sum_up);
        return false;
      }
      for (var i = 0; i < this.edited_paper.sections.length; i++) {
        if (this.question_sum_up(i).content != "valid") {
          console.log("question");
          console.log(this.question_sum_up(i));
          return false;
        }
      }
      console.log("here");
      return true;
    }
  },
  methods: {
    create_section() {
      this.edited_paper.sections.push({
        title: "",
        total_points: "0",
        questions: []
      });
    },
    question_sum_up(index) {
      //sum up of points assigned to each question and check if sum == total points of this section
      let section = this.edited_paper.sections[index];
      let sum = 0;
      for (var i = 0; !!section && i < section.questions.length; i++) {
        sum += parseInt(section.questions[i].point);
      }
      var tip =
        sum == section.total_points && !!section.total_points
          ? { color: "green", content: "valid" }
          : {
              color: "red",
              content:
                "Sum-up of points of questions: " +
                sum +
                " |Points assigned to this section: " +
                section.total_points
            };
      return tip;
    },
    drop_section(index) {
      //delete a section
      this.edited_paper.sections.splice(index, 1);
      if (this.cur_section == this.edited_paper.sections[index])
        this.cur_section = undefined;
    },
    drop_question(section, index) {
      //delete a question in selected question
      section.questions.splice(index, 1);
    },
    get_bank_id(id) {
      this.question_bank_id = id;
      this.process = "question";
    },
    get_selected_questions(questions) {
      let that = this;
      for (var i = 0; i < questions.length; i++) {
        axios.get("/api/questions/" + questions[i] + "/").then(response => {
          that.cur_section.questions.push({
            point: "",
            content: response.data
          });
          //after at least one question has been loaded, close the dialog
          this.adding_question = false;
        });
      }
    },
    submit() {
      this.$emit("save", JSON.parse(JSON.stringfy(this.edited_paper)));
      var result = JSON.parse(JSON.stringfy(this.edited_paper));
      for (var i = 0; i < result.sections.length; i++) {
        var section = result.sections[i];
        section["section_num"] = i + 1;
        for (var j = 0; j < section.questions.length; j++) {
          section.questions[j]["question_num"] = j + 1;
        }
      }
      if (this.id == -1) {
        axios
          .post("/api/papers/", result)
          .then(response => {
            alert("OK" + response.data);
          })
          .catch(error => {
            alert(error);
          });
      }
    },
    reset() {
      this.$refs.input.reset();
      this.edited_paper.sections.splice(0, this.edited_paper.sections.length);
    },
    cancel() {
      this.edited_paper = JSON.parse(JSON.stringfy(this.paper));
    },
    roman(num) {
      var n,
        m,
        str = "",
        i = 1000;
      for (; i > 0; i /= 10) {
        n = Math.floor(num / i); //向下取整
        m = n;
        switch (i) {
          case 1000: {
            if (m > 0) str += "M".repeat(n);
            num -= n * i; //减去
            break;
          }
          case 100: {
            if (n == 9) {
              str += "CM";
              m -= 9;
            }
            if (m >= 5) {
              str += "D";
              m -= 5;
            }
            if (m == 4) {
              str += "CD";
              m -= 4;
            }
            if (m > 0) str += "C".repeat(m);
            num -= n * i;
            break;
          }
          case 10: {
            if (n == 9) {
              str += "XC";
              m -= 9;
            }
            if (m >= 5) {
              str += "L";
              m -= 5;
            }
            if (m == 4) {
              str += "XL";
              m -= 4;
            }
            if (m > 0) str += "X".repeat(m);
            num -= n * i;
            break;
          }
          case 1: {
            if (n == 9) {
              str += "IX";
              m -= 9;
            }
            if (m >= 5) {
              str += "V";
              m -= 5;
            }
            if (m == 4) {
              str += "IV";
              m -= 4;
            }
            if (m > 0) str += "I".repeat(m);
            num -= n * i;
            break;
          }
        }
      }
      return str;
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
