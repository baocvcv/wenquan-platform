<template>
  <v-card>
    <v-list>
      <slot name="content" :question_data="question_data">
        <v-container class="pt-0 pb-0">
          <rich-text-editor readonly v-model="content">
          </rich-text-editor>
        </v-container>
      </slot>
      <slot name="answer" :question_data="question_data"></slot>
      <slot name="score" :question_data="question_data"></slot>
      <slot name="comment" :question_data="question_data"></slot>
      <slot name="others" :question_data="question_data"></slot>
    </v-list>
  </v-card>
</template>

<script>
import axios from "axios";
import RichTextEditor from "@/components/RichTextEditor.vue";

export default {
  name: "question-show",
  props: {
    id: {
      type: Number,
      default: null
    }
  },
  components: {
    "rich-text-editor": RichTextEditor
  },
  data: function() {
    return {
      question_data: {
        question_name: "Loading...",
        question_content: ""
      },
      content: null
    };
  },
  created() {
    if (this.id)
      axios
        .get("/api/questions/" + this.id + "/")
        .then(response => {
          this.question_data = response.data;
          this.parse();
        })
        .catch(err => {
          this.question_data = {
            question_name: "Error!",
            question_content: err.toString()
          };
        });
  },
  methods: {
    parse() {
      let content = "";
      if (this.question_data.question_type === "fill_blank") {
        let index;
        for (index in this.question_data.question_content) {
          content += this.question_data.question_content[index];
          if (index != this.question_data.question_content.length - 1) {
            content += "_____";
          }
        }
      } else {
        content = this.question_data.question_content;
      }
      this.content = content;
    }
  }
};
</script>
