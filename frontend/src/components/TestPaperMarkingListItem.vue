<template>
  <v-list-group v-if="!!paper_name">
    <template v-slot:activator>
      <v-list-item-title
        >{{ paper_name }} | Total records:
        {{ paper_records.length }}</v-list-item-title
      >
    </template>
    <v-list-item v-for="(record, key) in paper_records" :key="key">
      <v-list-item-content>
        <v-list-item-title
          ><span>{{ record.username }}</span> |
          <span v-if="record.need_judging" style="color: red; font-size: 80%"
            >Unmarked</span
          ><span v-else style="color: green; font-size: 80%;">Marked</span> |
          <span style="font-size: 80%"
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
        <slot name="button">
          <v-tooltip bottom :record_id="record.id">
            <template v-slot:activator="{ on }">
              <v-btn icon v-on="on" @click="$router.push('/admin/testmark/' + record.id)"
                ><v-icon>mdi-pen-plus</v-icon></v-btn
              >
            </template>
            <span>Mark</span>
          </v-tooltip>
        </slot>
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
      paper_name: "test-paper-list-item",
      paper_records: []
    };
  },
  created() {
    axios
      .get("/api/paper_records?paper=" + this.id, {
        headers: {
          Authorization: "Token " + this.$store.state.user.token
        }
      })
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
<style></style>
