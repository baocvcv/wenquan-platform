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
                            >
                                <question-list-item v-bind="question"></question-list-item>
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
            tags: ["Animal", "Insect"],
            difficulty: 2,
            type: "Single Choice",
            content: "Which of the following choice comes from part of an insect?\nasdasdasdasd adaasdasd\nasdaqrwnnfsfr\nasdasdasas\nwfweofibweofibweofibweofibweofibwe;oifbw;eofibwe;ofibwe;oifbw;eoifbw;eoifbw;eoifbw;eofibw;eoifbw;oeibf;wofibw;eoibfw;ofib"
        }
        let question_2 = {
            id: 2,
            tags: ["Math"],
            difficulty: 5,
            type: "Blank Filling",
            content: "TEST"
        }
        this.question_list.push(question_1);
        //this.question_list.push(question_2);
    }
}
</script>