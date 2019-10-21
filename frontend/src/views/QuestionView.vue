<template>
    <div class="question-view">
        <v-btn @click="test()">test</v-btn>
        <v-select :items="typeSelection" v-model="typeSelected" label="Choose Type"></v-select>
        <multiple-choice ref="multi" v-if="typeSelected=='Multiple Choice'"></multiple-choice>
    </div>
</template>

<script>
import MultipleChoice from "../components/MultipleChoice.vue";

export default {
    name: "question-view",
    components: {
        "multiple-choice": MultipleChoice
    },
    props: {

    },
    methods: {
        test() {
            this.$refs.multi.readonly=true;
            this.$refs.multi.updateData({
                "id": 12,
                "parents_node": [0,1],
                "question_change_time": "2019-10-15T01:11:21.754312Z",
                "question_name": "quesion2",
                "question_type": "multiple",
                "question_level": 0.5,
                "question_content": "人类的本质是?",
                "question_image": [""],
                "question_choice": ["A.复读机", "B.鸽子", "C.真香", "D.草履虫"],
                "question_ans": ["A","B","C"], 
                "question_ans_num": 3,
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