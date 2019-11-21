<template>
  <div id="single-choice-content">
    <v-form ref="input" v-model="valid">
      <v-row>
        <v-col cols="12" md="9">
          <rich-text-editor
            label="Content*"
            v-model="edited_question.question_content"
            :readonly="readonly"
            required
            ref="richtext"
          ></rich-text-editor>
          <v-list flat>
            <v-list-item two-line>
              <v-list-item-content align="left">
                <v-list-item-title>Choices</v-list-item-title>
                <v-list-item-subtitle
                  v-if="!readonly"
                  :style="
                    !!edited_question.question_ans
                      ? 'color: green;'
                      : 'color: red;'
                  "
                >
                  {{
                    !!edited_question.question_ans
                      ? "You have selected " +
                        edited_question.question_ans.name +
                        " as the right answer"
                      : "You haven't choose a right answer!"
                  }}
                </v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
            <v-list-item-group color="primary">
              <v-list-item
                v-for="(choice, i) in TF
                  ? tf_choice
                  : edited_question.question_choice"
                :key="i"
              >
                <v-list-item-icon>{{ choice.name }}</v-list-item-icon>
                <v-text-field
                  v-if="!TF"
                  v-model="choice.content"
                  placeholder="Enter content"
                  :rules="[v => !!v || 'Choice content is required!']"
                  :readonly="readonly"
                  required
                ></v-text-field>
                <v-tooltip top>
                  <template v-slot:activator="{ on }">
                    <v-btn
                      icon
                      small
                      @click="readonly ? () => {} : check_ans(choice)"
                      v-on="on"
                      ><v-icon
                        :color="
                          edited_question.question_ans == choice
                            ? 'green'
                            : 'red'
                        "
                        dark
                        >{{
                          edited_question.question_ans == choice
                            ? "mdi-check-circle"
                            : "mdi-close-circle"
                        }}
                      </v-icon></v-btn
                    >
                  </template>
                  <span>select as right answer</span>
                </v-tooltip>
                <v-tooltip top>
                  <template v-slot:activator="{ on }">
                    <v-btn
                      v-if="!readonly && !TF"
                      icon
                      small
                      @click="delete_choice(i)"
                      v-on="on"
                      ><v-icon color="red" dark>mdi-minus</v-icon></v-btn
                    >
                  </template>
                  <span>remove</span>
                </v-tooltip>
              </v-list-item>
            </v-list-item-group>
            <v-row>
              <v-btn
                v-if="!readonly && !TF"
                text
                height="50px"
                class="mx-2 create-choice-button ml-4 mr-4"
                @click="choice_num_up()"
                color="grey"
                >create new</v-btn
              >
            </v-row>
          </v-list>
          <v-textarea
            label="Analysis*"
            v-model="edited_question.question_solution"
            :rules="[v => !!v || 'Analysis is required!']"
            outlined
            auto-grow
            :readonly="readonly"
          ></v-textarea>
          <v-textarea
            label="Notes"
            v-model="edited_question.title"
            outlined
            :readonly="readonly"
            hint="Write down some notes if necessary"
          ></v-textarea>
        </v-col>
        <v-col>
          <p class="grey--text caption mb-1">Type:</p>
          <v-chip class="mb-4 mt-2">Single Choice</v-chip>
          <p class="grey--text caption mb-1">Difficulty:</p>
          <v-rating
            v-model="edited_question.difficulty"
            color="yellow darken-3"
            background-color="grey darken-1"
            :readonly="readonly"
            hover
            small
          ></v-rating>
        </v-col>
      </v-row>
      <v-row>
        <v-spacer></v-spacer>
        <v-btn v-if="!readonly" @click="cancel" text class="cancel-button">
          Cancel
        </v-btn>
        <v-btn
          class="mr-4 reset-button"
          text
          @click="reset()"
          v-if="!readonly && creation"
        >
          Reset
        </v-btn>
        <v-btn
          class="mr-4"
          color="primary"
          outlined
          @click="submit()"
          :disabled="
            !valid ||
              !edited_question.question_ans ||
              this.edited_question.question_content.length == 0
          "
          v-if="!readonly"
        >
          {{ creation ? "Create" : "Save" }}
        </v-btn>
      </v-row>
    </v-form>
  </div>
</template>

<script>
import RichTextEditor from "@/components/RichTextEditor.vue";
export default {
  name: "",
  props: {
    readonly: {
      type: Boolean,
      default: false
    },
    TF: {
      type: Boolean,
      default: false
    },
    creation: {
      type: Boolean,
      default: false
    }
  },
  components: {
    "rich-text-editor": RichTextEditor
  },
  data: function() {
    return {
      valid: false,
      edited_question: {
        id: -1,
        parents_node: [],
        question_level: 0,
        question_change_time: "",
        question_name: "",
        question_content: "",
        question_image: [],
        question_choice: [],
        question_ans: undefined,
        question_solution: ""
      },
      tf_choice: [{ name: "T", content: true }, { name: "F", content: false }],
      question: undefined
    };
  },
  created() {
    this.question = JSON.stringify(this.parse());
    let i;
    for (i = 0; i < 4; i++) {
      this.choice_num_up();
    }
  },
  methods: {
    choice_num_up() {
      let choice_num = this.edited_question.question_choice.length;
      this.edited_question.question_choice.push({
        name: String.fromCharCode(choice_num + 65),
        content: ""
      });
    },
    delete_choice(index) {
      if (
        this.edited_question.question_ans ==
        this.edited_question.question_choice[index]
      ) {
        this.edited_question.question_ans = undefined;
      }
      this.edited_question.question_choice.splice(index, 1);
      for (var i = 0; i < this.edited_question.question_choice.length; i++) {
        this.edited_question.question_choice[i].name = String.fromCharCode(
          65 + i
        );
      }
    },
    check_ans(choice) {
      this.edited_question.question_ans =
        this.edited_question.question_ans == choice ? undefined : choice;
    },
    updateData(input) {
      this.edited_question.id = input.id;
      this.edited_question.parents_node = input.parents_node;
      this.edited_question.question_level = input.question_level;
      this.edited_question.question_change_time = input.question_change_time;
      this.edited_question.question_name = input.question_name;
      this.edited_question.question_image = input.question_image;
      this.edited_question.question_solution = input.question_solution;
      this.edited_question.question_content = input.question_content;
      this.edited_question.question_ans = undefined;
      if (!this.TF) {
        var parsed = [];
        var origin = input.question_choice;
        for (var i = 0; i < origin.length; i++) {
          var id = String.fromCharCode(i + 65);
          var choice = {
            name: id,
            content: origin[i]
          };
          if (input.question_ans == id)
            this.edited_question.question_ans = choice;
          parsed.push(choice);
        }
        this.edited_question.question_choice = parsed;
      } else {
        this.edited_question.question_ans = input.question_ans
          ? this.tf_choice[0]
          : this.tf_choice[1];
      }
      this.question = JSON.stringify(this.parse());
    },
    parse() {
      var result = {
        id: this.edited_question.id,
        parents_node: this.edited_question.parents_node,
        question_change_time: this.edited_question.question_change_time,
        question_type: this.TF ? "TorF" : "single",
        question_level: this.edited_question.question_level,
        question_name: this.edited_question.question_name,
        question_image: this.edited_question.question_image,
        question_content: this.edited_question.question_content,
        question_solution: this.edited_question.question_solution
      };
      if (this.TF) {
        result["question_ans"] = this.edited_question.question_ans
          ? this.edited_question.question_ans.content
          : undefined;
      } else {
        var parsedChoice = [];
        var localChoice = this.edited_question.question_choice;
        for (var i = 0; i < localChoice.length; i++) {
          parsedChoice.push(localChoice[i].content);
        }
        result["question_ans"] = this.edited_question.question_ans
          ? this.edited_question.question_ans.name
          : undefined;
        result["question_choice"] = parsedChoice;
      }
      return result;
    },
    reset() {
      this.$refs.input.reset();
      this.edited_question.question_choice.splice(
        0,
        this.edited_question.question_choice.length
      );
      let i;
      for (i = 0; i < 4; i++) {
        this.choice_num_up();
      }
      this.edited_question.question_ans = undefined;
      this.$refs.richtext.reset();
      this.question = JSON.stringify(this.parse());
    },
    cancel() {
      this.updateData(JSON.parse(this.question));
      this.$emit("cancel");
    },
    submit() {
      this.$emit("submit", this.parse());
    },
    submitted() {
      this.question = JSON.stringify(this.parse());
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.create-choice-button {
  border-style: dashed;
  border-width: 1px;
  width: 100%;
}
</style>
