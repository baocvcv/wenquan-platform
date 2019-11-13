<template>
  <div>
    <v-card>
      <v-tabs show-arrows>
        <v-tabs-slider></v-tabs-slider>
        <v-tab>
          <v-icon left>mdi-earth</v-icon>
          Manage
        </v-tab>
        <v-tab>
          <v-icon left>mdi-pen-plus</v-icon>
          Marking
        </v-tab>
        <v-tab-item>
          <test-papers-list
            :title="
              $vuetify.breakpoint.smAndUp
                ? 'Browse and Create Test Papers'
                : 'Test Papers'
            "
          />
        </v-tab-item>
        <v-tab-item>
          <test-paper-marking-list
            :title="
              $vuetify.breakpoint.smAndUp
                ? 'Give marks and comment on students\' submits'
                : 'Mark'
            "
          />
        </v-tab-item>
      </v-tabs>
    </v-card>
  </div>
</template>

<script>
import TestPapersList from "@/components/TestPapersList.vue";
import TestPaperMarkingList from "@/components/TestPaperMarkingList.vue";

export default {
  name: "test-papers",
  props: {},
  components: {
    "test-papers-list": TestPapersList,
    "test-paper-marking-list": TestPaperMarkingList
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
