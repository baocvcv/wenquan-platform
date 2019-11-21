<template>
  <div id="question-banks">
    <v-card>
      <v-card-text>
        <v-tabs>
          <v-tab>
            <v-icon left>mdi-earth</v-icon>
            Explore
          </v-tab>
          <v-tab>
            <v-icon left>mdi-account</v-icon>
            MyBank
          </v-tab>
          <v-tab-item>
            <question-banks-list
              :flat="true"
              :explore="true"
              :admin="false"
              :title="
                $vuetify.breakpoint.smAndUp
                  ? 'Explore Your Favourite Question Banks'
                  : 'Explore'
              "
              @force-update="forceUpdate"
            ></question-banks-list>
          </v-tab-item>
          <v-tab-item>
            <question-banks-list
              :flat="true"
              :mybank="true"
              :admin="false"
              :bankIDs="$store.state.user.question_banks"
              :title="'MyBank'"
              ref="my-bank"
            ></question-banks-list>
          </v-tab-item>
        </v-tabs>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import QuestionBanksList from "@/components/QuestionBanksList.vue";

export default {
  name: "question-banks",
  components: {
    "question-banks-list": QuestionBanksList
  },
  methods: {
    forceUpdate() {
      this.$refs["my-bank"].$forceUpdate();
    }
  }
};
</script>
