<template>
  <div>
    <question-banks-list
      :readonly="readonly"
      title="Question Banks"
    ></question-banks-list>
  </div>
</template>

<script>
import QuestionBanksList from "@/components/QuestionBanksList.vue";

export default {
  name: "",
  data: function() {
    return {
      readonly: false
    };
  },
  components: {
    "question-banks-list": QuestionBanksList
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
