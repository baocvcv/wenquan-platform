<template>
    <div id="question-list">
        <v-card>
            <v-card-title>Question List</v-card-title>
            <v-app-bar flat clipped-left>
                <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
                <div class="flex-grow-1"></div>
                    <v-menu open-on-hover top offset-y>
                        <template v-slot:activator="{ on }">
                            <v-btn icon>
                                <v-icon>mdi-filter</v-icon>
                            </v-btn>
                        </template>
                    </v-menu>
                    <v-menu open-on-hover top offset-y>
                        <template v-slot:activator="{ on }">
                            <v-btn icon>
                                <v-icon>mdi-sort</v-icon>
                            </v-btn>
                        </template>
                    </v-menu>
                    <v-btn
                    v-if="editable"
                    text
                    >Create</v-btn>
            </v-app-bar>
            <v-card-text>
                <v-row>
                    <v-col
                        v-show="drawer" 
                        cols="12"
                        md="4"
                        sm="6"
                        >
                        <tree-view></tree-view>
                    </v-col>
                    <v-col
                        :cols="drawer && !$vuetify.breakpoint.xsOnly ? 6 : 12"
                        :md="drawer ? 8 : 12"
                    >
                        <v-row dense>
                            <v-col 
                            v-for="question in question_list"
                            :key="question.id"
                            cols="12"
                            >
                                <question-list-item :question="question"></question-list-item>
                            </v-col>
                        </v-row>
                    </v-col>
                </v-row>
            </v-card-text>
        </v-card>
    </div>
</template>

<script>
import tree_view from "@/components/TreeView.vue";
import question_list_item from "@/components/QuestionListItem.vue"

export default {
    name: "question-list",
    props: {
        editable: Boolean
    },
    components: {
        "tree-view": tree_view,
        "question-list-item": question_list_item
    },
    data: () => ({
        drawer: null,
        question_list: []
    }),
    mounted() {
        let question_1 = {
            id: 1,
            question_change_time: "2019-10-22",
            question_name: "Name 1",
            question_type: "single",
            question_level: 2,
            question_content: "What's the result of 1 + 1?",
            question_image: [""],
            question_choice: ["A.1", "B.2", "C.3", "D.4"],
            question_ans: "B",
            question_solution: "It is trival.",
            question_tags: ["Math", "Arithmetics"]
        }
        let question_2 = {
            id: 12,
            parents_node: [0,1],
            question_change_time: "2019-10-15T01:11:21.754312Z",
            question_name: "quesion2",
            question_type: "multiple",
            question_level: 0.5,
            question_content: "人类的本质是?",
            question_image: [""],
            question_choice: ["A.复读机", "B.鸽子", "C.真香", "D.草履虫"],
            question_ans: ["A","B","C"], 
            question_ans_num: 3,
            question_solution: "某一时刻被观测时, 人类会坍缩为A,B,C中某一种情况",
            question_tags: ["Tag1", "Tag2"]
        }
        this.question_list.push(question_1);
        this.question_list.push(question_2);
    }
}
</script>