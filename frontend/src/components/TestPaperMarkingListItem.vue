<template>
  <v-list-group v-if="!!paper_name">
    <template v-slot:activator>
      <v-list-item-title>{{ paper_name }}</v-list-item-title>
    </template>
    <v-list-item v-for="(record, key) in paper_records" :key="key">
      <v-list-item-content>
        <v-row align="center">
          <v-col>{{ record.id }}</v-col>
        </v-row>
      </v-list-item-content>
      <v-list-item-action> </v-list-item-action>
    </v-list-item>
  </v-list-group>
</template>

<script>
import axios from "axios";
export default {
  name: "test-paper-marking-list-item",
  props: {
    id: -1
  },
  data: function() {
    return {
      paper_name: "",
      paper_records: []
    };
  },
  created() {
    axios.get("/api/paper_records?paper=" + this.id).then(response => {
      let all_records = response.data;
      for (var i = 0; i < all_records.length; i++) {
        if (all_records[i].is_active)
          this.paper_records.unshift(all_records[i]);
        else this.paper_records.push(all_records[i]);
      }
      if (all_records.length != 0) this.paper_name = all_records[0].paper_name;
    });
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
