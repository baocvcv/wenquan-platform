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
            <v-card-title>
              Create A Question
              <v-btn right absolute icon @click="create_question_dialog = false"
                ><v-icon>mdi-close</v-icon></v-btn
              >
            </v-card-title>
            <v-card-text>
              <question
                :initData="null"
                :root_id="root_id"
                creation
                @submit="create"
                @cancel="create_question_dialog = false"
              ></question>
            </v-card-text>
          </v-card>
        </v-dialog>
      </v-app-bar>
      <v-card-text>
        <vue-progress-bar style="position: relative;"></vue-progress-bar>
        <v-row>
          <v-col v-show="drawer" cols="12" md="4" sm="6" id="drawer-col">
            <tree-view
              :rootID="root_id"
              v-model="tree_selection"
              editable
            ></tree-view>
          </v-col>
          <v-col
            :cols="drawer && !$vuetify.breakpoint.xsOnly ? 6 : 12"
            :md="drawer ? 8 : 12"
          >
            <p
              class="caption grey--text text-right mt-0 mb-0 pr-1"
              transition="fade-transition"
            >
              {{ process }}
            </p>
            <v-row dense>
              <v-col
                v-for="question in shown_questions"
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
      question_list: {},
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
      is_selecting: false,
      process: "",
      shown_questions: [],
      question_indices: [],
      root_id: -1
    };
  },
  watch: {
    tree_selection() {
      this.process = "Fetching data from server...";
      let selected_node_id = [];
      let i;
      for (i in this.tree_selection) {
        selected_node_id.push(this.tree_selection[i].id);
      }
      if (selected_node_id.length === 0) {
        this.shown_questions = [];
        let index;
        for (index in this.question_list) {
          this.shown_questions.push(this.question_list[index]);
        }
        this.process = "Total Count: " + this.shown_questions.length;
        return;
      }
      const headers = {
        Authorization: "Token " + this.$store.state.user.token
      };
      axios
        .post(
          "/api/nodes_question/",
          { nodes_id: selected_node_id },
          { headers: headers }
        )
        .then(response => {
          this.question_indices = response.data;
        });
    },
    question_indices() {
      this.shown_questions = [];
      let count = 0;
      let all_count = this.question_indices.length;
      let lock = false;
      let i;
      this.$Progress.start();
      console.log(this.process);
      let process_on = () => {
        while (lock);
        lock = true;
        count++;
        this.$Progress.increase((1 / (all_count + 0.0001)) * 100);
        this.process = "Loading questions: " + count + " / " + all_count;
        if (count == all_count) {
          this.process = "Total Count: " + all_count;
          this.$Progress.finish();
        }
        lock = false;
      };
      if (this.question_indices.length === 0) {
        this.$Progress.finish();
        this.process = "Total Count: " + 0;
      }
      for (i in this.question_indices) {
        let index = this.question_indices[i];
        if (this.question_list.hasOwnProperty(index)) {
          this.shown_questions.push(this.question_list[index]);
          process_on();
        } else {
          const headers = {
            Authorization: "Token " + this.$store.state.user.token
          };
          axios
            .get("/api/questions/" + index + "/", { headers: headers })
            .then(response => {
              this.shown_questions.push(response.data);
              this.question_list[index] = response.data;
              process_on();
            });
        }
      }
    }
  },
  created() {
    if (this.select) this.is_selecting = true;
    this.process = "Fetching data from server...";
    const headers = {
      Authorization: "Token " + this.$store.state.user.token
    };
    axios
      .get("/api/question_banks/" + this.id + "/", { headers: headers })
      .then(response => {
        this.question_indices = JSON.parse(
          JSON.stringify(response.data.questions)
        );
        this.root_id = response.data.root_id;
      })
      .catch(error => {
        console.log(error);
      });
  },
  methods: {
    reset_filter() {
      this.type_filter = [];
      this.level_min_filter = 0;
      this.level_max_filter = 5;
    },
    create(question_id) {
      const headers = {
        Authorization: "Token " + this.$store.state.user.token
      };
      axios
        .get("/api/questions/" + question_id + "/", { headers: headers })
        .then(response => {
          this.question_list[question_id] = response.data;
          console.log(this.question_list[question_id]);
          console.log(response.data.parents_node);
          console.log(this.tree_selection);
          if (this.tree_selection.length == 0) {
            this.shown_questions.push(response.data);
            this.create_question_dialog = false;
            return;
          }
          let node_index;
          for (node_index in response.data.parents_node) {
            let selected_index;
            for (selected_index in this.tree_selection) {
              if (
                this.tree_selection[selected_index] ===
                response.data.parents_node[node_index]
              )
                this.shown_questions.push(response.data);
            }
          }
          this.create_question_dialog = false;
        })
        .catch(error => {
          console.log(error);
        });
    },
    cancel_select() {
      this.selected_questions = [];
      this.$emit("cancel-select");
      //this.is_selecting = false;
    },
    done_select() {
      this.$emit("done-select", this.selected_questions);
      //this.is_selecting = false;
    }
  }
};
</script>

<style scoped>
#drawer-col {
  border-right: 1px solid rgb(226, 226, 226);
}
</style>
