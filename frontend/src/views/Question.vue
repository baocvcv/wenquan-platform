<template>
    <div class="question">
        <v-card>
            <v-card-title v-if="!creation">
                Question
                <v-btn
                    absolute
                    right
                    icon
                    @click="change_edit_mode"
                    v-if="!creation && _editable"
                >
                    <v-icon>mdi-pencil</v-icon>
                </v-btn>
            </v-card-title>
            <v-row>
                <v-col cols="6">
                    <v-select
                        :items="typeSelection"
                        v-model="typeSelected"
                        label="Choose Type"
                        v-if="creation"
                    ></v-select>
                </v-col>
            </v-row>
            <question-multiple-choice
                ref="multiple"
                v-if="typeSelected=='multiple'"
                :readonly="!creation && !(_editable && edit_mode)"
                v-on:submit="submit"
                v-on:cancel="cancel"
                :creation="creation"
            ></question-multiple-choice>
            <question-single-choice
                ref="single"
                v-if="typeSelected=='single'"
                :readonly="!creation && !(_editable && edit_mode)"
                v-on:submit="submit"
                v-on:cancel="cancel"
                :creation="creation"
            ></question-single-choice>
            <question-single-choice
                ref="TorF"
                v-if="typeSelected=='TorF'"
                TF
                :readonly="!creation && !(_editable && edit_mode)"
                v-on:submit="submit"
                v-on:cancel="cancel"
                :creation="creation"
            ></question-single-choice>
            <question-brief-answer
                ref="brief_ans"
                v-if="typeSelected=='brief_ans'"
                :readonly="!creation && !(_editable && edit_mode)"
                v-on:submit="submit"
                v-on:cancel="cancel"
                :creation="creation"
            ></question-brief-answer>
            <question-fill-in-blank
                ref="fill_blank"
                v-if="typeSelected=='fill_blank'"
                :readonly="!creation && !(_editable && edit_mode)"
                v-on:submit="submit"
                v-on:cancel="cancel"
                :creation="creation"
            ></question-fill-in-blank>
        </v-card>
    </div>
</template>

<script>
import QuestionMultipleChoice from "@/components/QuestionMultipleChoice.vue";
import QuestionSingleChoice from "@/components/QuestionSingleChoice.vue"
import QuestionBriefAnswer from "@/components/QuestionBriefAnswer.vue"
import QuestionFillInBlank from "@/components/QuestionFillInBlank.vue";
import axios from "axios";

export default {
    name: "question-view",
    components: {
        "question-multiple-choice": QuestionMultipleChoice,
        "question-single-choice": QuestionSingleChoice,
        "question-brief-answer": QuestionBriefAnswer,
		"question-fill-in-blank": QuestionFillInBlank
    },
    props: {
        bankID: {
            type: Array,
            default: null
        },
        editable: {
            type: Boolean,
            default: false
        },
        creation: {
            type: Boolean,
            default: false
        },
        questionID: {
            type: Number,
            default: -1
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
    created() {
        if (!this.creation)
        {
            let url;
            if (this.questionID == -1)
            {
                url="/api/questions/" + this.$route.params.id + "/";
            }
            else
            {
                url = "/api/questions/" + this.questionID + "/";
            }
            axios.get(url)
                .then((response) => {
                    this.initData = response.data;
                })
                .catch((error) => {
                    console.log(error);
                })
        }
    },
    computed: {
        _editable() {
            if (! this.creation && this.$route.fullPath.search("/questions/") != -1 && this.$store.state.user.user_type != "Student")
                return true;
            return this.editable;
        }
    },
    mounted() {
        if(this.initData)
            this.typeSelected = this.initData.question_type;
    },
    updated() {
        if(this.initData)
        {
            this.$refs[this.initData.question_type].updateData(this.initData);
        }
    },
    methods: {
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
        },
        submit(info) {
            if(info.parents_node.length==0 && this.bankID){
                //New question
                info.parents_node=this.bankID;
                axios.post("/api/questions/",[info]).then(response => {
                    this.edit_mode = false;
                    this.$emit("submit");
                }).catch(err => {
                    console.log(info);
                    console.log(err);
                });
            }else{
                //Edit question
                axios.put("/api/questions/"+info.id.toString()+"/",[info]).then(response => {
                    this.$refs[this.typeSelected].submitted();
                    this.edit_mode = false;
                    this.$emit("submit");
                }).catch(err => {
                    console.log(info);
                    console.log(err);
                })
            }
        },
        cancel() {
            this.edit_mode = false;
            this.$emit("cancel");
        },
        change_edit_mode() {
            if (this.edit_mode)
                this.$refs[this.typeSelected].cancel();
            else
                this.edit_mode = true;
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
            edit_mode: false,
            initData: null
        };
    }
}
</script>
