<template>
    <question-show :id="3">
        <template v-slot:content="{ question_data }">
            <v-list-item>
                <span v-if="question_data.question_type == 'fill_blank'">
                    <span v-for="(item,index) in question_data.question_content" :key="item">
                        {{ item }}
                        <span v-if="index < question_data.question_blank_num">______</span>
                    </span>
                </span>
                <span v-else>
                    {{ question_data.question_content }}
                </span>
            </v-list-item>
        </template>
        <template v-slot:answer="{ question_data }">
            <v-list-item v-if="question_data.question_type == 'fill_blank'">
                <v-row>
                    <v-col
                        v-for="index in question_data.question_blank_num" :key="index"
                        cols="12"
                        md="4"
                        lg="3"
                    >
                        <v-text-field
                            :label="index.toString()"
                            v-model="answer[index-1]">
                        </v-text-field>
                    </v-col>
                </v-row>
            </v-list-item>
        </template>
        <template v-slot:button="{ question_data }">
            <v-btn class="mx-2 my-2" color="success">Submit</v-btn>
        </template>
    </question-show>
</template>

<script>
import QuestionShow from "./QuestionShow.vue"

export default {
    name: "question-solve",
    components: {
        "question-show": QuestionShow
    },
    data: function() {
        return {
            answer: [],
            score: [],
            comment: ""
        }
    }
}
</script>