<template>
    <div class="paper-solve">
        <v-row>
            <v-col cols="12" lg="3" sm="4">
                <v-tabs>
                    <v-tab
                        v-for="item in paper.sections"
                        :key="item"
                    >
                        {{ item.title }}
                    </v-tab>
                    <v-tab-item
                        v-for="item in paper.sections"
                        :key="item"
                    >
                        <v-row>
                            <v-col cols="2" v-for="(question,index) in item.questions"
                                :key="index"
                            >
                                <v-btn icon outlined>
                                    {{ index + 1 }}
                                </v-btn>
                            </v-col>
                        </v-row>
                    </v-tab-item>
                </v-tabs>
            </v-col>
            <v-col cols="12" lg="9" sm="8">
                <question-solve></question-solve>
            </v-col>
        </v-row>
    </div>    
</template>

<script>
import QuestionSolve from "@/components/QuestionSolve.vue";

export default {
    name: "paper-solve",
    components: {
        "question-solve": QuestionSolve
    },
    props: {
        initData: {
            type: Object,
            default: null
        }
    },
    data: function() {
        return {
            paper: {
                sections: []
            },
            current_question: -1
        };
    }
}
</script>