<template>
  <div>
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
        <v-btn
          color="primary"
          elevation="0"
          class="ml-2"
          @click="create_test_paper = true"
          >Create</v-btn
        >
      </v-toolbar>
      <v-card-text class="pt-0">
        <p
          class="caption grey--text text-right mt-0 mb-0 pr-1"
          transition="fade-transition"
        >
          {{ process }}
        </p>
        <v-row justify="left">
          <v-col
            v-for="(paper, key) in test_papers"
            :key="key"
            cols="12"
            lg="4"
            sm="12"
          >
            <test-papers-list-item :test_paper="paper" :readonly="readonly"
              ><v-btn icon dark
                ><v-icon>mdi-heart</v-icon></v-btn
              ></test-papers-list-item
            >
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>

    <v-dialog
      v-model="create_test_paper"
      hide-overlay
      fullscreen
      transition="dialog-bottom-transition"
    >
      <v-card>
        <v-toolbar flat>
          <v-toolbar-title>Create a Test Paper</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn icon @click="create_test_paper = false">
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-toolbar>
        <test-paper create v-on:create-response="create_response" />
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import TestPaper from "@/components/TestPaper.vue";
import TestPapersListItem from "@/components/TestPapersListItem.vue";
import axios from "axios";
export default {
  name: "test-papers-list",
  props: {
    title: {
      type: String,
      default: "Test Papers"
    },
    readonly: {
      type: Boolean,
      default: false
    }
  },
  components: {
    "test-paper": TestPaper,
    "test-papers-list-item": TestPapersListItem
  },
  data: function() {
    return {
      create_test_paper: false,
      process: "",
      test_papers: []
    };
  },
  mounted() {
    this.update_data();
  },
  methods: {
    update_data() {
      this.process = "fetching data ...";
            const headers = {
        Authorization: "Token " + this.$store.state.user.token
      };
      axios
        .get("/api/papers/", {headers: headers})
        .then(response => {
          this.test_papers = response.data;
          this.process = "total count: " + this.test_papers.length;
        })
        .catch(error => {
          this.process = error;
        });
    },
    create_response(result) {
      if (result) this.update_data();
      this.create_test_paper = false;
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
