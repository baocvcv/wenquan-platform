<template>
  <div>
    <v-form ref="input" v-model="valid">
      <v-text-field
        label="Title"
        v-model="edited_question.question_name"
        :readonly="readonly"
        outlined
      ></v-text-field>
      <v-textarea
        label="Content"
        v-model="edited_question.question_content"
        :rules="[v => !!v || 'Question content is required!']"
        :readonly="readonly"
        auto-grow
        outlined
        required
      ></v-textarea>
      <image-uploader
        ref="uploader"
        v-model="edited_question.question_image"
        width="50%"
        label="picture"
        :readonly="readonly"
        multiple
        placeholder="Upload an image if necessary"
      ></image-uploader>
      <v-list flat>
        <v-list-item two-line>
          <v-list-item-content align="left">
            <v-list-item-title>Choices</v-list-item-title>
            <v-list-item-subtitle
              v-if="!readonly"
              :style="!!edited_question.question_ans ? 'color: green;' : 'color: red;'"
              >
              {{ !!edited_question.question_ans ? "You have selected " + edited_question.question_ans.name + " as the right answer": "You haven't a right answer!" }}
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
        <v-list-item-group color="primary">
          <v-list-item
            v-for="(choice, i) in TF ? tf_choice : edited_question.question_choice"
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
                    :color="edited_question.question_ans == choice ? 'green' : 'red'"
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
        <v-btn
          v-if="!readonly && !TF"
          class="mx-2"
          block
          tile
          dark
          color="green"
          @click="choice_num_up()"
          >create new</v-btn
        >
      </v-list>
      <br />
      <v-textarea
        label="Analysis"
        v-model="edited_question.question_solution"
        :rules="[v => !!v || 'Analysis is required!']"
        :readonly="readonly"
        auto-grow
        outlined
        required
      ></v-textarea>
      <v-list-item>
        <span>Difficulty:</span>
        <v-rating
          v-model="edited_question.question_level"
          color="yellow darken-3"
          background-color="grey darken-1"
          :readonly="readonly"
          hover
        ></v-rating>
      </v-list-item>
      <div class="flex-grow-1"></div>
      <v-btn
        v-if="!readonly"
        :disabled="!valid || !edited_question.question_ans"
        color="success"
        class="mr-4"
        @click="submit()"
        >
          {{ creation? "Create" : "Save" }}
        </v-btn>
      <v-btn v-if="!readonly && creation" color="error" class="mr-4" @click="reset()"
        >Reset</v-btn
      >
      <v-btn v-if="!readonly" @click="cancel">
        Cancel
      </v-btn>
    </v-form>
  </div>
</template>

<script>
import ImageUploader from "./ImageUploader.vue";
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
    "image-uploader": ImageUploader
  },
  data: function() {
    return {
      valid: false,
      question: {
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
      edited_question: null
    };
  },
  created() {
    this.edited_question = JSON.parse(JSON.stringify(this.question));
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
      if (this.edited_question.question_ans == this.edited_question.question_choice[index]) {
        this.edited_question.question_ans = undefined;
      }
      this.edited_question.question_choice.splice(index, 1);
      for (var i = 0; i < this.edited_question.question_choice.length; i++) {
        this.edited_question.question_choice[i].name = String.fromCharCode(65 + i);
      }
    },
    check_ans(choice) {
      this.edited_question.question_ans = this.edited_question.question_ans == choice ? undefined : choice;
    },
    updateData(input) {
      this.question.id = input.id;
      this.question.parents_node = input.parents_node;
      this.question.question_level = input.question_level;
      this.question.question_change_time = input.question_change_time;
      this.question.question_name = input.question_name;
      this.question.question_image = input.question_image;
      this.question.question_solution = input.question_solution;
      this.question.question_content = input.question_content;
      if (!this.TF) {
        var parsed = [];
        var origin = input.question_choice;
        for (var i = 0; i < origin.length; i++) {
          var id = String.fromCharCode(i + 65);
          var choice = {
            name: id,
            content: origin[i]
          };
          if (input.question_ans == id) this.question.question_ans = choice;
          parsed.push(choice);
        }
        this.question.question_choice = parsed;
      } else {
        this.question.question_ans = input.question_ans
          ? this.tf_choice[0]
          : this.tf_choice[1];
      }
      this.edited_question = JSON.parse(JSON.stringify(this.question));

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
        result["question_ans"] = this.edited_question.question_ans.content;
      } else {
        var parsedChoice = [];
        var localChoice = this.edited_question.question_choice;
        for (var i = 0; i < localChoice.length; i++) {
          parsedChoice.push(localChoice[i].content);
        }
        result["question_ans"] = this.edited_question.question_ans.name;
        result["question_choice"] = parsedChoice;
      }
      return result;
    },
    reset() {
      this.$refs.input.reset();
      this.edited_question.question_choice.splice(0, this.question.question_choice.length);
      this.edited_question.question_ans = undefined;
      this.$refs.uploader.reset();
      this.question = JSON.parse(JSON.stringify(this.edited_question));
    },
    cancel() {
      this.edited_question = JSON.parse(JSON.stringify(this.question));
      this.$emit("cancel");
    },
    submit() {
      this.$emit("submit", this.parse());
    },
    submitted() {
      this.question = JSON.parse(JSON.stringify(this.edited_question));
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
