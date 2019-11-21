<template>
  <question-show :id="id">
    <template v-slot:answer="{ question_data }">
      <v-list-item v-if="question_data.question_type == 'fill_blank'">
        <v-row>
          <v-col
            v-for="index in question_data.question_blank_num"
            :key="index"
            cols="12"
            md="4"
            lg="3"
          >
            <v-text-field
              :label="index.toString()"
              v-model="answer[index - 1]"
              :readonly="readonly"
            >
            </v-text-field>
            <!-- index starts from 1 -->
            <slot
              :name="'correct-' + index.toString()"
              :question_data="question_data"
            ></slot>
          </v-col>
        </v-row>
      </v-list-item>
      <v-list-item v-if="question_data.question_type == 'single'">
        <v-radio-group v-model="answer">
          <v-radio
            v-for="(item, index) in question_data.question_choice"
            :key="item"
            :value="String.fromCharCode(index + 65)"
            :label="String.fromCharCode(index + 65) + '. ' + item"
            :readonly="readonly"
          ></v-radio>
        </v-radio-group>
      </v-list-item>
      <v-list-item v-if="question_data.question_type == 'TorF'">
        <v-radio-group v-model="answer">
          <v-radio :value="true" label="T"></v-radio>
          <v-radio :value="false" label="F"></v-radio>
        </v-radio-group>
      </v-list-item>
      <v-list-item v-if="question_data.question_type == 'multiple'">
        <v-container>
          <v-checkbox
            v-for="(item, index) in question_data.question_choice"
            :key="item"
            :value="String.fromCharCode(index + 65)"
            :label="String.fromCharCode(index + 65) + '. ' + item"
            v-model="answer"
            :readonly="readonly"
          ></v-checkbox>
        </v-container>
      </v-list-item>
      <v-list-item v-if="question_data.question_type == 'brief_ans'">
        <v-textarea
          label="Answer"
          v-model="answer"
          outlined
          auto-grow
          :readonly="readonly"
        ></v-textarea>
      </v-list-item>
      <slot name="correct" :question_data="question_data"></slot>
    </template>
    <template v-slot:standard-answer="{ question_data }">
      <slot name="standard-answer" :question_data="question_data"></slot>
    </template>
    <template v-slot:score="{ question_data }">
      <slot name="score" :question_data="question_data"></slot>
    </template>
    <template v-slot:comment="{ question_data }">
      <slot name="comment" :question_data="question_data"></slot>
    </template>
    <template v-slot:others="{ question_data }">
      <slot name="others" :question_data="question_data"></slot>
    </template>
  </question-show>
</template>

<script>
import QuestionShow from "./QuestionShow.vue";

export default {
  name: "question-solve",
  components: {
    "question-show": QuestionShow
  },
  props: {
    answer: [],
    id: {
      type: Number,
      default: null
    },
    readonly: {
      type: Boolean,
      default: false
    }
  },
  watch: {
    answer: {
      handler(newVal) {
        this.$emit("change", newVal);
      },
      deep: true
    }
  },
  model: {
    prop: "answer",
    event: "change"
  }
};
</script>
