<template>
<div id="question-bank">
    <h1>Question Bank</h1>
    <v-card>
        <v-card-title>Profile        
            <v-btn
                absolute
                right
                icon
            ><v-icon>mdi-pencil</v-icon></v-btn>
        </v-card-title>
        <v-card-text>
            <span>Brief</span>
            <v-textarea
            ></v-textarea>
        </v-card-text>
    </v-card>
    <question-list :editable="true"></question-list>
</div>
</template>

<script>
import question_list from "@/components/QuestionList.vue";

export default {
    name: "question-bank",
    components: {
        "question-list": question_list,
    },
    data: () => ({

    })
}
</script>