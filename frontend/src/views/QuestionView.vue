<template>
    <div class="question-view">
        <v-btn @click="test()">test</v-btn>
        <v-select :items="typeSelection" v-model="typeSelected" label="Choose Type"></v-select>
        <multiple-choice ref="multi" v-if="typeSelected=='Multiple Choice'"></multiple-choice>
        <single-choice ref="single" v-if="typeSelected=='Single Choice'"></single-choice>
        <single-choice ref="TorF" v-if="typeSelected=='T or F'" TF></single-choice>
        <brief-answer ref="brief" v-if="typeSelected=='Brief Answer'"></brief-answer>
    </div>
</template>

<script>
import MultipleChoice from "../components/MultipleChoice.vue";
import SingleChoice from "../components/SingleChoice.vue"
import BriefAnswer from "../components/BriefAnswer.vue"

export default {
    name: "question-view",
    components: {
        "multiple-choice": MultipleChoice,
        "single-choice": SingleChoice,
        "brief-answer": BriefAnswer,
    },
    props: {

    },
    methods: {
        test() {
            this.$refs.brief.readonly=true;
            this.$refs.brief.updateData({
                "id": 1,
                "parents_node": [0],
                "question_change_time": "2019-10-15T01:11:21.754312Z",
                "question_name": "quesion1",
                "question_type": "single",
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
            typeSelection: ["Single Choice","Multiple Choice","T or F","Brief Answer"],
            typeSelected: null,
        };
    }
}
</script>