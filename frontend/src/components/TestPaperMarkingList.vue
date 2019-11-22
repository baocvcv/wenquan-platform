<template>
  <div class="test-paper-marking-list">
    <vue-element-loading :active="loading" is-full-screen></vue-element-loading>
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
          <test-paper-marking-list-item
            v-for="(paper, key) in papers"
            :key="key"
            ref="items"
            :id="paper.id"
            v-on:show="count"
          />
        </v-list>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import TestPaperMarkingListItem from "@/components/TestPaperMarkingListItem.vue";
import axios from "axios";
import VueElementLoading from "vue-element-loading";
export default {
  name: "test-paper-marking-list",
  props: {
    title: {
      type: String,
      default: "Marking"
    }
  },
  components: {
    "test-paper-marking-list-item": TestPaperMarkingListItem,
    "vue-element-loading": VueElementLoading
  },
  data: function() {
    return {
      process: "loading",
      papers: [],
      loading: false,
      latest: true
    };
  },
  created() {
    this.loading = true;
    axios
      .get("/api/papers/", {
        headers: {
          Authorization: "Token " + this.$store.state.user.token
        }
      })
      .then(response => {
        this.papers = response.data;
        this.process = "Total count: 0";
      })
      .catch(error => {
        this.process = "Oops!" + error;
      })
      .then(() => {
        this.loading = false;
      });
  },
  methods: {
    count() {
      let cnt = 0;
      for (var i = 0; i < this.$refs.items.length; i++) {
        if (this.$refs.items[i].show()) cnt++;
      }
      this.process = "Total count: " + cnt;
      return cnt;
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
