<template>
    <div class="question-view">
        <v-select
            :items="typeSelection"
            v-model="typeSelected"
            label="Choose Type"
            v-if="!readonly">
        </v-select>
        <question-multiple-choice
            ref="multiple"
            v-if="typeSelected=='multiple'"
            v-on:submit="submit"
            :readonly="readonly"
        ></question-multiple-choice>
        <question-single-choice
            ref="single"
            v-if="typeSelected=='single'"
            v-on:submit="submit"
            :readonly="readonly"
        ></question-single-choice>
        <question-single-choice
            ref="TorF"
            v-if="typeSelected=='TorF'"
            v-on:submit="submit"
            TF
            :readonly="readonly"
        ></question-single-choice>
        <question-brief-answer
            ref="brief_ans"
            v-if="typeSelected=='brief_ans'"
            v-on:submit="submit"
            :readonly="readonly"
        ></question-brief-answer>
        <question-fill-in-blank
            ref="fill_blank"
            v-if="typeSelected=='fill_blank'"
            v-on:submit="submit"
            :readonly="readonly"
        ></question-fill-in-blank>
    </div>
</template>

<script>
import QuestionMultipleChoice from "./QuestionMultipleChoice.vue";
import QuestionSingleChoice from "./QuestionSingleChoice.vue"
import QuestionBriefAnswer from "./QuestionBriefAnswer.vue"
import QuestionFillInBlank from "./QuestionFillInBlank.vue";

export default {
    name: "question-view",
    components: {
        "question-multiple-choice": QuestionMultipleChoice,
        "question-single-choice": QuestionSingleChoice,
        "question-brief-answer": QuestionBriefAnswer,
		"question-fill-in-blank": QuestionFillInBlank
    },
    props: {
        readonly: {
            type: Boolean,
            default: false
        },
        initData: {
            type: Object,
            default: null
        },
        bankID: {
            type: Array,
            default: null
        }
    },
    watch: {
        initData: function(newOne){
            if(!newOne)
                this.typeSelected = null;
            else {
                this.typeSelected = this.initData.question_type;
                //then updated will be called
            }
        }
    },
    mounted() {
        if(this.initData)
            this.typeSelected = this.initData.question_type;
    },
    updated() {
        if(this.initData)
            this.$refs[this.initData.question_type].updateData(this.initData);
    },
    methods: {
        submit(info) {
            if(info.parents_node.length==0 && this.bankID){
                //New question
                info.parents_node=this.bankID;
                axios.post("/api/questions/",[info]).then(response => {
                    this.$emit("submit",info);
                }).catch(err => {
                    console.log(info);
                    console.log(err);
                });
            }else{
                //Edit question
                axios.put("/api/questions/"+info.id.toString()+"/",[info]).then(response => {
                    this.$emit("submit",info);
                }).catch(err => {
                    console.log(info);
                    console.log(err);
                })
            }
        },
        test() {
            this.$refs.brief.readonly=true;
            this.$refs.brief.updateData({
                "id": 1,
                "parents_node": [0],
                "question_change_time": "2019-10-15T01:11:21.754312Z",
                "question_name": "quesion1",
                "question_type": "brief_ans",
                "question_level": 0.5,
                "question_content": "人类的本质是?",
                "question_image": [""],
                "question_ans": "复读机", 
                "question_solution": "某一时刻被观测时, 人类会坍缩为A,B,C中某一种情况"
            });
        }
    },
    data: function() {
        return {
            typeSelection: [
                {text:"Single Choice", value:"single"},
                {text:"Multiple Choice", value:"multiple"},
                {text:"T or F", value:"TorF"},
                {text:"Brief Answer", value:"brief_ans"},
                {text:"Fill in Blank", value:"fill_blank"}
            ],
            typeSelected: null,
        };
    }
}
</script>
