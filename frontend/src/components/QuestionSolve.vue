<template>
    <question-show :id="3">
        <template v-slot:button>
            <v-list-item>
                A Slot Example
            </v-list-item>
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