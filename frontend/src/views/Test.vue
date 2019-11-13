<template>
    <div class="test">
        <paper-solve v-if="paper_data" :initData="paper_data"></paper-solve>
        <vue-element-loading :active="loading" is-full-screen></vue-element-loading>
    </div>
</template>

<script>
import PaperSolve from "@/components/PaperSolve.vue";
import VueElementLoading from "vue-element-loading";
import axios from "axios";

export default {
    name: "test",
    components: {
        "paper-solve": PaperSolve,
        "vue-element-loading": VueElementLoading
    },
    created() {
        this.loading = true;
        let id = this.$route.params.id;
        axios
        .get("/api/papers/" + id + "/")
        .then(async response => {
            let result = response.data;
            for (var i = 0; i < result.sections.length; i++) {
            result.sections[i] = await axios.get(
                "/api/paper_sections/" + result.sections[i].id + "/"
            );
            result.sections[i] = result.sections[i].data;
            for (var j = 0; j < result.sections[i].questions.length; j++) {
                let question = result.sections[i].questions[j];
                let tmp_data = await axios.get(
                "/api/questions/" + question.id + "/"
                );
                question["content"] = tmp_data.data;
            }
            }
            this.paper_data = result;
            this.loading = false;
        })
        .catch(error => {
            console.log(error);
        })
        .then(() => {
            this.loading = false;
        });
    },
    data: function() {
        return {
            loading: false,
            paper_data: null
        };
    }
}
</script>