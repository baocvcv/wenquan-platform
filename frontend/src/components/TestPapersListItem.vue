<template>
  <div>
    <v-card>
      <v-card-title>{{ test_paper.title }}</v-card-title>
      <v-divider></v-divider>
      <v-card-text>
        <p>Total Points: {{ test_paper.total_point }} points</p>
        <p>Time Limit: {{ test_paper.time_limit }} min</p>
        <p>Status: {{ test_paper.status }}</p>
      </v-card-text>

      <v-card-actions>
        <v-tooltip bottom>
          <template v-slot:activator="{ on }">
            <v-btn
              v-show="!readonly"
              text
              color="primary"
              v-on="on"
              @click="change_paper_status"
              >{{ change_paper_status_btn_text }}</v-btn
            >
          </template>
          <span>Change status of this test paper to {{ opposite_status }}</span>
        </v-tooltip>
        <v-spacer></v-spacer>
        <v-tooltip bottom>
          <template v-slot:activator="{ on }">
            <v-hover v-slot:default="{ hover }">
              <v-btn
                icon
                v-on="on"
                @click="$router.push('/test/' + test_paper.id)"
                ><v-icon :color="hover ? 'primary' : 'grey lighten-1'"
                  >mdi-fountain-pen-tip</v-icon
                ></v-btn
              >
            </v-hover>
          </template>
          <span>Test</span>
        </v-tooltip>
        <v-tooltip bottom>
          <template v-slot:activator="{ on }">
            <v-hover v-slot:default="{ hover }">
              <v-btn
                v-show="!readonly"
                icon
                v-on="on"
                @click="$router.push('/admin/testpapers/' + test_paper.id)"
                ><v-icon :color="hover ? 'primary' : 'grey lighten-1'"
                  >mdi-file-eye-outline</v-icon
                ></v-btn
              >
            </v-hover>
          </template>
          <span>view this test paper</span>
        </v-tooltip>
        <v-tooltip bottom>
          <template v-slot:activator="{ on }">
            <v-hover v-slot:default="{ hover }">
              <v-btn
                v-show="!readonly"
                icon
                v-on="on"
                @click="delete_test_paper = true"
                ><v-icon :color="hover ? 'error' : 'grey lighten-1'"
                  >mdi-trash-can-outline</v-icon
                ></v-btn
              >
            </v-hover>
          </template>
          <span>delete</span>
        </v-tooltip>
      </v-card-actions>
    </v-card>

    <v-dialog v-model="delete_test_paper" max-width="300px">
      <v-card>
        <v-card-title>Warning</v-card-title>
        <v-divider></v-divider>
        <v-card-text align="center">
          <span
            >Are you sure to delete this test paper({{
              test_paper.title
            }})</span
          >
        </v-card-text>
        <v-card-actions>
          <v-btn text @click="delete_confirmed">Confirm</v-btn>
          <v-btn text @click="delete_test_paper = false">Cancel</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "test-papers-list-item",
  props: {
    test_paper: {
      type: Object,
      default: () => {}
    },
    readonly: {
      type: Boolean,
      default: false
    }
  },
  data: function() {
    return {
      delete_test_paper: false
    };
  },
  computed: {
    change_paper_status_btn_text: function() {
      return this.test_paper["status"] == "drafted" ? "publish" : "drafted";
    },
    opposite_status() {
      return this.test_paper["status"] == "drafted" ? "published" : "drafted";
    }
  },
  methods: {
    delete_confirmed() {
      const headers = {
        Authorization: "Token " + this.$store.state.user.token
      };
      axios
        .delete("/api/papers/" + this.test_paper.id + "/", { headers: headers })
        .then(response => {
          console.log(response);
          this.$emit("delete");
        })
        .catch(error => {
          console.log(error);
        })
        .then(() => {
          this.delete_test_paper = false;
        });
    },
    change_paper_status() {
      const headers = {
        Authorization: "Token " + this.$store.state.user.token
      };
      axios
        .put(
          "/api/papers/" + this.test_paper.id + "/",
          {
            change_status: this.opposite_status
          },
          { headers: headers }
        )
        .then(() => {
          this.$notify({
            text: "Change test paper state to " + this.opposite_status,
            type: "success"
          });
          this.test_paper["status"] = this.opposite_status;
        })
        .catch(error => {
          this.$notify({
            title: "error",
            text: "Oops..." + error,
            type: "error"
          });
        });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
