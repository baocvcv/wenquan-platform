<template>
    <div class="question-view-outer">
        <question-view ref="view" :readonly="readonly" :initData="questionData"></question-view>
    </div>
</template>

<script>
import View from "../components/QuestionView.vue";
import axios from "axios";

export default {
    name: "question-outer",
    components: {
        "question-view": View
    },
    created() {
        if(this.$route.params.id){
            let url="/api/questions/"+this.$route.params.id+"/";
            axios.get(url).then(response => {
                this.questionData = JSON.parse(response);
                this.readonly = false;
            }).catch(err => {
                console.log(err);
            })
        }
    },
    data: function () {
        return {
            questionData: null,
            readonly: false,
        };
    }
}
</script>