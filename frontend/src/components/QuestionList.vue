<template>
  <div id="question-list">
    <v-card>
      <v-card-title>
        Question List
        <div class="flex-grow-1"></div>
        <v-btn v-if="is_selecting" text @click="cancel_select">
          Cancel
        </v-btn>
        <v-btn v-if="is_selecting" text @click="done_select">
          Done
        </v-btn>
      </v-card-title>
      <v-app-bar flat clipped-left>
        <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
        <div class="flex-grow-1"></div>
        <v-text-field
          flat
          hide-details
          label="Search"
          prepend-inner-icon="mdi-magnify"
          clearable
        ></v-text-field>
        <v-menu
          bottom
          offset-y
          transition="slide-y-transition"
          :close-on-content-click="false"
        >
          <template v-slot:activator="{ on }">
            <v-btn icon v-on="on">
              <v-icon>mdi-filter</v-icon>
            </v-btn>
          </template>
          <v-sheet>
            <v-container>
              <v-btn absolute right icon @click="reset_filter">
                <v-icon>mdi-autorenew</v-icon>
              </v-btn>
              <span class="grey--text caption">Type</span>
              <v-select
                v-model="type_filter"
                :items="question_types"
                chips
                label="Type"
                multiple
              >
                <template v-slot:selection="{ item, index }">
                  <v-chip v-if="index === 0">
                    <span>{{ item }}</span>
                  </v-chip>
                  <span v-if="index === 1" class="grey--text caption"
                    >(+{{ type_filter.length - 1 }} others)</span
                  >
                </template>
              </v-select>
              <span class="grey--text caption">Difficulty</span>
              <v-row>
                <v-col>
                  <v-select
                    v-model="level_min_filter"
                    :items="[1, 2, 3, 4, 5]"
                    label="Low Bound"
                    outlined
                  ></v-select>
                </v-col>
                <v-col>
                  <v-select
                    v-model="level_max_filter"
                    :items="[1, 2, 3, 4, 5]"
                    label="Up Bound"
                    outlined
                  ></v-select>
                </v-col>
              </v-row>
            </v-container>
          </v-sheet>
        </v-menu>
        <v-menu offset-y transition="slide-y-transition">
          <template v-slot:activator="{ on }">
            <v-btn icon v-on="on">
              <v-icon>mdi-sort</v-icon>
            </v-btn>
          </template>
          <v-list>
            <v-list-item v-for="(item, index) in sort_menu" :key="index">
              <v-list-item-title>{{ item }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
        <v-dialog
          v-model="create_question_dialog"
          fullscreen
          hide-overlay
          transition="dialog-bottom-transition"
        >
          <template v-slot:activator="{ on }">
            <v-btn
              v-show="editable && $vuetify.breakpoint.mdAndUp"
              color="primary"
              elevation="0"
              v-on="on"
              >Create</v-btn
            >
            <v-btn
              v-show="editable && !$vuetify.breakpoint.mdAndUp"
              color="primary"
              elevation="0"
              v-on="on"
            >
              <v-icon>mdi-plus</v-icon>
            </v-btn>
          </template>
          <v-card>
            <v-card-title>Create A Question</v-card-title>
            <v-card-text>
              <question
                :initData="null"
                :bankID="[id]"
                creation
                @submit="create"
                @cancel="create_question_dialog = false"
              ></question>
            </v-card-text>
          </v-card>
        </v-dialog>
      </v-app-bar>
      <v-card-text>
        <v-row>
          <v-col v-show="drawer" cols="12" md="4" sm="6">
            <tree-view
              :bankID="id"
              v-model="tree_selection"
              editable
            ></tree-view>
          </v-col>
          <v-col
            :cols="drawer && !$vuetify.breakpoint.xsOnly ? 6 : 12"
            :md="drawer ? 8 : 12"
          >
            <v-row dense>
              <v-col
                v-for="question in question_list"
                :key="question.id"
                cols="12"
              >
                <v-row align="center">
                  <v-checkbox
                    v-if="select"
                    v-model="selected_questions"
                    :value="question.id"
                    hide-details
                    class="shrink mr-2 mt-0"
                  ></v-checkbox>
                  <v-col>
                    <question-list-item
                      :question="question"
                      :dialog="dialog"
                    ></question-list-item>
                  </v-col>
                </v-row>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import tree_view from "@/components/TreeView.vue";
import question_list_item from "@/components/QuestionListItem.vue";
import question from "@/views/Question.vue";
import axios from "axios";

export default {
  name: "question-list",
  props: {
    editable: {
      type: Boolean,
      default: false
    },
    id: {
      type: Number,
      default: -1
    },
    select: {
      type: Boolean,
      default: false
    },
    questions: {
      type: Array,
      default: () => []
    },
    dialog: {
      type: Boolean,
      default: false
    }
  },
  components: {
    "tree-view": tree_view,
    "question-list-item": question_list_item,
    question: question
  },
  data: function() {
    return {
      create_question_dialog: false,
      type_filter: [],
      level_min_filter: 0,
      level_max_filter: 5,
      drawer: null,
      question_list: [],
      tree_selection: [],
      sort_menu: ["Popularity", "Level"],
      keyword: "",
      question_types: [
        "Single",
        "Multiple",
        "T/F",
        "Blank Filling",
        "Brief Answer"
      ],
      selected_questions: [],
      is_selecting: false
    };
  },
  mounted() {
    if (this.select) this.is_selecting = true;
    let load_questions = () => {
      let question_id_index;
      for (question_id_index in questions) {
        axios
          .get("/api/questions/" + questions[question_id_index] + "/")
          .then(response => {
            this.question_list.push(response.data);
          })
          .catch(error => {
            console.log(error);
          });
      }
    };
    let questions;
    if (this.questions.length == 0) {
      axios
        .get("/api/question_banks/" + this.id + "/")
        .then(response => {
          questions = response.data.questions;
          load_questions();
        })
        .catch(error => {
          console.log(error);
        });
    } else {
      questions = this.questions;
      load_questions();
    }
  },
  methods: {
    reset_filter() {
      this.type_filter = [];
      this.level_min_filter = 0;
      this.level_max_filter = 5;
    },
    create(question_id) {
      axios
        .get("/api/questions/" + question_id + "/")
        .then(response => {
          this.question_list.push(response.data);
          this.create_question_dialog = false;
        })
        .catch(error => {
          console.log(error);
        });
    },
    cancel_select() {
      this.selected_questions = [];
      this.$emit("cancel-select");
      this.is_selecting = false;
    },
    done_select() {
      this.$emit("done-select", this.selected_questions);
      this.is_selecting = false;
    }
  }
};
</script>
