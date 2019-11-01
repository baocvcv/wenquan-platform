<template>
  <div class="fill-in-blank-component">
    <v-form ref="form" v-model="valid">
      <v-text-field
        label="Title"
        v-model="edited_data.title"
        outlined
        :readonly="readonly"
      ></v-text-field>
      <v-textarea
        label="Content"
        v-model="edited_data.content"
        :rules="[v => !!v || 'Question content is required!']"
        placeholder="Use '_' to represent blanks"
        outlined
        auto-grow
        :readonly="readonly"
      ></v-textarea>
      <image-uploader
        ref="uploader"
        v-model="edited_data.image"
        width="50%"
        label="picture"
        :readonly="readonly"
        multiple
        placeholder="Upload an image if necessary"
      ></image-uploader>
      <v-list flat>
        <v-list-item>
          <v-list-item-content align="left">
            <v-list-item-title>Answers</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item-group color="primary">
          <v-list-item v-for="index in blankNum" :key="index">
            <v-text-field
              placeholder="Enter answer"
              v-model="edited_data.answers[index - 1]"
              :rules="[v => !!v || 'Answer content is required!']"
              :readonly="readonly"
            ></v-text-field>
          </v-list-item>
        </v-list-item-group>
      </v-list>
      <br />
      <v-textarea
        label="Analysis"
        v-model="edited_data.analysis"
        :rules="[v => !!v || 'Analysis is required!']"
        outlined
        auto-grow
        :readonly="readonly"
      ></v-textarea>
      <v-list-item>
        <span>Difficulty:</span>
        <v-rating
          v-model="edited_data.difficulty"
          color="yellow darken-3"
          background-color="grey darken-1"
          :readonly="readonly"
          hover
        ></v-rating>
      </v-list-item>
      <v-btn
        class="mr-4"
        color="success"
        @click="submit()"
        :disabled="!canSubmit"
        v-if="!readonly"
      >
        Submit
      </v-btn>
      <v-btn
        class="mr-4"
        color="error"
        @click="reset()"
        v-if="!readonly && creation"
      >
        Reset
      </v-btn>
      <v-btn v-if="!readonly">
        Cancel
      </v-btn>
    </v-form>
  </div>
</template>

<script>
import ImageUploader from "./ImageUploader.vue";
export default {
  name: "fill-in-blank",
  components: {
    "image-uploader": ImageUploader
  },
  props: {
    readonly: {
      type: Boolean,
      default: false
    },
    creation: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    blankNum() {
      if (this.edited_data.content)
        return this.edited_data.content.split(/_+/).length - 1;
      else return 0;
    },
    canSubmit() {
      return this.valid;
    }
  },
  created() {
    this.edited_data = JSON.parse(JSON.stringify(this.data));
  },
  methods: {
    submit() {
      this.$emit("submit", this.parse());
    },
    reset() {
      this.$refs.form.reset();
      this.edited_data.answers = [];
      this.edited_data.image = [];
      this.data = JSON.parse(JSON.stringify(this.edited_data));
    },
    cancel() {
      this.edited_data = JSON.parse(JSON.stringify(this.data));
      this.$emit("cancel");
    },
    submitted() {
      this.data = JSON.parse(JSON.stringify(this.edited_data));
    },
    updateData(input) {
      //parse data input from backend
      this.data.id = input.id;
      this.data.parents = input.parents_node;
      this.data.change_time = input.question_change_time;
      this.data.title = input.question_name;
      this.data.content = input.question_content.join("______");
      this.data.image = input.question_image;
      this.data.analysis = input.question_solution;
      this.data.difficulty = input.question_level;
      this.data.answers = input.question_ans;
      this.edited_data = JSON.parse(JSON.stringify(this.data));
    },
    parse() {
      let result = {
        id: this.edited_data.id,
        parents_node: this.edited_data.parents,
        question_change_time: this.edited_data.change_time,
        question_name: this.edited_data.title,
        question_type: "fill_blank",
        question_level: this.edited_data.difficulty,
        question_content: this.edited_data.content.split(/_+/),
        question_blank_num: this.blankNum,
        question_image: this.edited_data.image,
        question_ans: this.edited_data.answers,
        question_solution: this.edited_data.analysis
      };
      if (result.question_ans.length > result.question_blank_num)
        result.question_ans.splice(
          result.question_blank_num,
          result.question_ans.length - result.question_blank_num
        );
      return result;
    }
  },
  data: function() {
    return {
      data: {
        id: -1,
        parents: [],
        change_time: "",
        title: "",
        content: "",
        image: [],
        answers: [],
        analysis: "",
        difficulty: 0
      },
      edited_data: null,
      valid: false
    };
  }
};
</script>
