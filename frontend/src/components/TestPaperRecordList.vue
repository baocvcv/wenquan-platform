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
        <test-paper-marking-list-item
          v-for="(paper, key) in papers"
          :key="key"
          :id="paper"
          readonly
        >
          <template v-slot:button="{ record_id }">
            <v-tooltip bottom>
              <template v-slot:activator="{ on }">
                <v-btn
                  icon
                  v-on="on"
                  @click="$router.push('/paper_record/' + record_id)"
                  ><v-icon>mdi-eye</v-icon></v-btn
                >
              </template>
              <span>View</span>
            </v-tooltip>
          </template>
        </test-paper-marking-list-item>
      </v-list>
    </v-card-text>
  </v-card>
</template>

<script>
import TestPaperMarkingListItem from "@/components/TestPaperMarkingListItem.vue";
import axios from "axios";
export default {
  name: "test-paper-marking-list",
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
      process: "loading",
      papers: []
    };
  },
  created() {
    axios
      .get("/api/paper_records/", {
        headers: {
          Authorization: "Token " + this.$store.state.user.token
        }
      })
      .then(response => {
        let raw = response.data;
        this.papers = [];
        raw.forEach(element => {
          if (this.papers.indexOf(element.paper_id) == -1)
            this.papers.push(element.paper_id);
        });
        this.process = "Total count: " + this.papers.length;
      })
      .catch(error => {
        this.process = "Oops!" + error;
      });
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
