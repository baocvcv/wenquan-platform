<template>
  <v-card>
    <v-card-text>
      <v-tabs v-if="!practicing">
        <v-tab>
          <v-icon left>mdi-finance</v-icon>
          Practice
        </v-tab>
        <v-tab :disabled="practicing">
          <v-icon left>mdi-clock-outline</v-icon>
          Test
        </v-tab>
        <v-tab-item>
          <practice v-on:practicing="start_practice" />
        </v-tab-item>
        <v-tab-item>
          <test-papers-list
            :title="
              $vuetify.breakpoint.smAndUp
                ? 'Choose a Test Paper to Simulate'
                : 'Test'
            "
            readonly
          />
        </v-tab-item>
      </v-tabs>
      <paper-solve v-if="practicing" :initData="paper" />
    </v-card-text>
  </v-card>
</template>

<script>
import Practice from "@/components/Practice.vue";
import TestPapersList from "@/components/TestPapersList.vue";
import PaperSolve from "@/components/PaperSolve.vue";
export default {
  name: "learn",
  data: function() {
    return {
      practicing: false,
      paper: undefined
    };
  },
  components: {
    practice: Practice,
    "test-papers-list": TestPapersList,
    "paper-solve": PaperSolve
  },
  methods: {
    start_practice(paper) {
      this.paper = paper;
      this.practicing = true;
    }
  },
  beforeRouteLeave(to, from, next) {
    if (this.practicing) {
      const answer = window.confirm(
        "Do you really want to leave? You are practicing."
      );
      if (answer) next();
      else next(false);
    } else next();
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
