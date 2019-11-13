<template>
  <v-list-group v-if="!!paper_name">
    <template v-slot:activator>
      <v-list-item-title>{{ paper_name }}</v-list-item-title>
    </template>
    <v-list-item v-for="(record, key) in paper_records" :key="key">
      <v-list-item-content>
        <v-list-item-title
          ><span>{{ record.username }}</span> |
          <span v-if="record.need_judging" class="unmarked">Unmarked</span
          ><span v-else class="marked">Marked</span> |
          <span class="score"
            >Score: {{ record.user_total_point }}/{{
              record.paper_total_point
            }}</span
          ></v-list-item-title
        >
        <v-list-item-subtitle
          v-text="record.record_time"
        ></v-list-item-subtitle>
      </v-list-item-content>
      <v-list-item-action>
        <v-tooltip bottom>
          <template v-slot:activator="{ on }">
            <v-btn icon v-on="on" @click="$router.push('/')"
              ><v-icon>mdi-pen-plus</v-icon></v-btn
            >
          </template>
          <span>Mark</span>
        </v-tooltip>
      </v-list-item-action>
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
    axios
      .get("/api/paper_records?paper=" + this.id)
      .then(response => {
        let all_records = response.data;
        for (var i = 0; i < all_records.length; i++) {
          if (all_records[i].need_judging)
            this.paper_records.unshift(all_records[i]);
          else this.paper_records.push(all_records[i]);
        }
        if (all_records.length != 0)
          this.paper_name = all_records[0].paper_name;
      })
      .catch(error => {
        console.log(error);
      });
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.unmarked: {
  color: red;
  font-size: 70%;
}
.marked: {
  color: green;
  font-size: 70%;
}
.score: {
  font-size: 70%;
}
</style>
