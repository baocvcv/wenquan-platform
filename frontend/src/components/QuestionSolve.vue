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
    }
}
</script>