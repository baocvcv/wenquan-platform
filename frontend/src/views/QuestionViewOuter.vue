<template>
    <div class="question-view-outer">
        <question-view ref="view" :readonly="readonly" :initData="questionData" :bankID="bankID"></question-view>
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
        if(this.$route.params.id && this.$route.fullPath.search("question")!=-1){
            let url="/api/questions/"+this.$route.params.id+"/";
            axios.get(url).then(response => {
                this.questionData = JSON.parse(response);
                this.readonly = false;
            }).catch(err => {
                console.log(err);
            })
        }
        if(this.$route.params.id && this.$route.fullPath.search("create_question")!=-1){
            this.bankID=[parseInt(this.$route.params.id)]
        }
    },
    data: function () {
        return {
            questionData: null,
            readonly: false,
            bankID: null
        };
    }
}
</script>