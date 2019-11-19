<template>
    <div class="test">
	    <slot name="marking" :paper_data="paper_data">
        <paper-solve v-if="paper_data" :initData="paper_data" @submit="submit"></paper-solve>
		</slot>
        <vue-element-loading :active="loading" is-full-screen></vue-element-loading>
        <v-dialog v-model="msg_dialog" max-width=600px>
            <v-card>
                <v-card-title>
                    Warning
                </v-card-title>
                <v-card-text>
                    {{ msg }}
                </v-card-text>
                <v-card-action>
                    <v-btn outlined @click="msg_dialog = false">
                        OK
                    </v-btn>
                </v-card-action>
            </v-card>
        </v-dialog>
    </div>
</template>

<script>
import PaperSolve from "@/components/PaperSolve.vue";
import VueElementLoading from "vue-element-loading";
import axios from "axios";

export default {
    name: "test",
	props: {
	  id: {
		type: Number,
		default: -1
	  }
	},
    components: {
        "paper-solve": PaperSolve,
        "vue-element-loading": VueElementLoading
    },
    created() {
        this.loading = true;
        let id = this.id == -1 ? this.$route.params.id : this.id;
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

            //start a new record
            let record = await axios.post("/api/paper_records/",{
                paper_id: id,
                is_timed: true
            },{
                headers:{
                    Authorization: "Token " + this.$store.state.user.token
                }
            });

            this.record_id = record.data.id;

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
            paper_data: null,
            record_id: null,
            msg_dialog: false,
            msg: ""
        };
    },
    methods: {
        submit(result) {
            result.paper_id = this.$route.params.id;
            result.action = "finish";
            this.loading = true;
            axios.post("/api/paper_records/" + this.record_id + "/",result)
                .then(response => {
                    this.loading = false;
                    this.$router.push("/learn");
                })
                .catch(err => {
                    console.log(err);
                    this.msg = "Due to network error, submit failed. Please try again later.";
                    this.msg_dialog = true;
                    this.loading = false;
                });
        }
    }
}
</script>
