<template>
  <div class="brief-answer-component">
    <v-form ref="form" v-model="valid">
      <v-row>
        <v-col cols="12" md="9">
          <rich-text-editor
            label="Content*"
            v-model="edited_data.content"
            :readonly="readonly"
            required
            ref="richtext"
          ></rich-text-editor>
          <v-textarea
            label="Answer*"
            v-model="edited_data.answer"
            :rules="[v => !!v || 'Answer is required!']"
            outlined
            auto-grow
            :readonly="readonly"
          ></v-textarea>
          <v-textarea
            label="Analysis*"
            v-model="edited_data.analysis"
            :rules="[v => !!v || 'Analysis is required!']"
            outlined
            auto-grow
            :readonly="readonly"
          ></v-textarea>
          <v-textarea
            label="Notes"
            v-model="edited_data.title"
            outlined
            :readonly="readonly"
            hint="Write down some notes if necessary"
          ></v-textarea>
        </v-col>
        <v-col>
          <p class="grey--text caption mb-1">Type:</p>
          <v-chip class="mb-4 mt-2">Brief Answer</v-chip>
          <p class="grey--text caption mb-1">Difficulty:</p>
          <v-rating
            v-model="edited_data.difficulty"
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
          :disabled="!canSubmit"
          v-if="!readonly"
        >
          Submit
        </v-btn>
      </v-row>
    </v-form>
  </div>
</template>

<script>
import RichTextEditor from "@/components/RichTextEditor.vue";

export default {
  name: "brief-answer",
  components: {
    "rich-text-editor": RichTextEditor
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
    canSubmit() {
      return this.valid && this.edited_data.content.length != 0;
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
      this.$refs.richtext.reset();
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
      this.data.content = input.question_content;
      this.data.image = input.question_image;
      this.data.analysis = input.question_solution;
      this.data.difficulty = input.question_level;
      this.data.answer = input.question_ans;
      this.edited_data = JSON.parse(JSON.stringify(this.data));
    },
    parse() {
      let result = {
        id: this.edited_data.id,
        parents_node: this.edited_data.parents,
        question_change_time: this.edited_data.change_time,
        question_name: this.edited_data.title,
        question_type: "brief_ans",
        question_level: this.edited_data.difficulty,
        question_content: this.edited_data.content,
        question_image: this.edited_data.image,
        question_choice: [],
        question_ans: this.edited_data.answer,
        question_solution: this.edited_data.analysis
      };
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
        answer: "",
        analysis: "",
        difficulty: 0
      },
      edited_data: null,
      valid: false
    };
  }
};
</script>
