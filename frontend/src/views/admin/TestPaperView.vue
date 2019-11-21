<template>
  <div>
    <vue-element-loading :active="loading" is-full-screen></vue-element-loading>
    <test-paper :paper="paper" v-show="!loading" />
  </div>
</template>

<script>
import TestPaper from "@/components/TestPaper.vue";
import axios from "axios";
import VueElementLoading from "vue-element-loading";
export default {
  name: "test-paper-view",
  data: function() {
    return {
      loading: false,
      paper: undefined
    };
  },
  components: {
    "test-paper": TestPaper,
    "vue-element-loading": VueElementLoading
  },
  created() {
    this.loading = true;
    let id = this.$route.params.id;
    const headers = {
      Authorization: "Token " + this.$store.state.user.token
    };
    axios
      .get("/api/papers/" + id + "/", { headers: headers })
      .then(async response => {
        let result = response.data;
        for (var i = 0; i < result.sections.length; i++) {
          result.sections[i] = await axios.get(
            "/api/paper_sections/" + result.sections[i].id + "/",
            { headers: headers }
          );
          result.sections[i] = result.sections[i].data;
          for (var j = 0; j < result.sections[i].questions.length; j++) {
            let question = result.sections[i].questions[j];
            let tmp_data = await axios.get(
              "/api/questions/" + question.id + "/",
              { headers: headers }
            );
            question["content"] = tmp_data.data;
          }
        }
		result.time_limit = result.time_limit/60;
        this.paper = result;
        this.loading = false;
      })
      .catch(error => {
        console.log(error);
      })
      .then(() => {
        this.loading = false;
      });
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
