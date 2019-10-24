<template>
  <div>
    <v-form ref="input" v-model="valid">
      <v-text-field
        label="Title"
        v-model="question_name"
        :readonly="readonly"
        outlined
      ></v-text-field>
      <v-textarea
        label="Content"
        v-model="question_content"
        :rules="[v => !!v || 'Question content is required!']"
        :readonly="readonly"
        auto-grow
        outlined
        required
      ></v-textarea>
      <image-uploader
        ref="uploader"
        v-model="question_image"
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
              :style="!!question_ans ? 'color: green;' : 'color: red;'"
              >You have chosen
              {{ !!question_ans ? question_ans.name : "none" }}
              as the right answer
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
        <v-list-item-group color="primary">
          <v-list-item
            v-for="(choice, i) in TF ? tf_choice : question_choice"
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
                    :color="question_ans == choice ? 'green' : 'red'"
                    dark
                    >{{
                      question_ans == choice
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
        label="Analyse"
        v-model="question_solution"
        :rules="[v => !!v || 'Analyse is required!']"
        :readonly="readonly"
        auto-grow
        outlined
        required
      ></v-textarea>
      <v-list-item>
        <span>Difficulty:</span>
        <v-rating
          v-model="question_level"
          color="yellow darken-3"
          background-color="grey darken-1"
          :readonly="readonly"
          half-increments
          hover
        ></v-rating>
      </v-list-item>
      <v-btn
        v-if="!readonly"
        :disabled="!valid || !question_ans"
        color="success"
        class="mr-4"
        @click="submit()"
        >Submit</v-btn
      >
      <v-btn v-if="!readonly" color="error" class="mr-4" @click="reset()"
        >Reset</v-btn
      >
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
    }
  },
  components: {
    "image-uploader": ImageUploader
  },
  data: function() {
    return {
      valid: false,
      id: -1,
      parents_node: [],
      question_level: 0,
      question_change_time: "",
      question_name: "",
      question_content: "",
      question_image: [],
      question_choice: [],
      question_ans: undefined,
      question_solution: "",
      tf_choice: [{ name: "T", content: true }, { name: "F", content: false }]
    };
  },
  methods: {
    choice_num_up() {
      let choice_num = this.question_choice.length;
      this.question_choice.push({
        name: String.fromCharCode(choice_num + 65),
        content: ""
      });
    },
    delete_choice(index) {
      if (this.question_ans == this.question_choice[index]) {
        this.question_ans = undefined;
      }
      this.question_choice.splice(index, 1);
      for (var i = 0; i < this.question_choice.length; i++) {
        this.question_choice[i].name = String.fromCharCode(65 + i);
      }
    },
    check_ans(choice) {
      this.question_ans = this.question_ans == choice ? undefined : choice;
    },
    updateData(input) {
      var parsed = [];
      var origin = input.question_choice;
      for (var i = 0; i < origin.length; i++) {
        var id = String.fromCharCode(i + 65);
        var choice = {
          name: id,
          content: origin[i]
        };
        if (input.question_ans == id) this.question_ans = choice;
        parsed.push(choice);
      }
      this.id = input.id;
      this.parents_node = input.parents_node;
      this.question_level = input.question_level;
      this.question_change_time = input.question_change_time;
      this.question_name = input.question_name;
      this.question_image = input.question_image;
      this.question_choice = parsed;
      this.question_solution = input.question_solution;
      this.question_content = input.question_content;
    },
    parse() {
      var result = {
        id: this.id,
        parents_node: this.parents_node,
        question_change_time: this.question_change_time,
        question_type: this.TF ? "TorF" : "single",
        question_level: this.question_level,
        question_name: this.question_name,
        question_image: this.question_image,
        question_content: this.question_content,
        question_solution: this.question_solution
      };
      if (this.TF) {
        result["question_ans"] = this.question_ans.content;
      } else {
        var parsedChoice = [];
        var localChoice = this.question_choice;
        for (var i = 0; i < localChoice.length; i++) {
          parsedChoice.push(localChoice[i].content);
        }
        result["question_ans"] = this.question_ans.name;
        result["question_choice"] = parsedChoice;
      }
      return result;
    },
    reset() {
      this.$refs.input.reset();
      this.question_choice.splice(0, this.question_choice.length);
      this.question_ans = undefined;
      this.$refs.uploader.reset();
    },
    submit() {
      this.$emit("submit",this.parse());
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
