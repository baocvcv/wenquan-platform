<template>
  <v-card>
    <v-toolbar flat>
      <v-toolbar-title>{{ title }}</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-text-field
        flat
        hide-details
        label="Search"
        prepend-inner-icon="mdi-magnify"
        clearable
      ></v-text-field>
    </v-toolbar>
    <v-card-text class="pt-0">
      <p
        class="caption grey--text text-right mt-0 mb-0 pr-1"
        transition="fade-transition"
      >
        {{ process }}
      </p>
      <v-list>
        <test-paper-marking-list-item />
      </v-list>
    </v-card-text>
  </v-card>
</template>

<script>
import TestPaperMarkingListItem from "@/components/TestPaperMarkingListItem.vue";
export default {
  name: "",
  props: {
    title: {
      type: String,
      default: "Marking"
    }
  },
  components: {
    "test-paper-marking-list-item": TestPaperMarkingListItem
  },
  data: function() {
    return {
      process: "loading"
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
