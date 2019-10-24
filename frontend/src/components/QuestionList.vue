<template>
    <div id="question-list">
        <v-card>
            <v-card-title>Question List</v-card-title>
            <v-app-bar flat clipped-left>
                <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
                <div class="flex-grow-1"></div>
                    <v-text-field
                        flat
                        hide-details
                        label="Search"
                        prepend-inner-icon="mdi-magnify"
                        clearable
                    ></v-text-field>
                    <v-menu 
                        bottom 
                        offset-y 
                        transition="slide-y-transition"
                        :close-on-content-click="false"
                    >
                        <template v-slot:activator="{ on }">
                            <v-btn icon v-on="on">
                                <v-icon>mdi-filter</v-icon>
                            </v-btn>
                        </template>
                        <v-sheet>
                            <v-container>
                                <v-btn
                                    absolute
                                    right
                                    icon
                                    @click="reset_filter"
                                >
                                    <v-icon>mdi-autorenew</v-icon>
                                </v-btn>
                                <span class="grey--text caption">Type</span>
                                <v-select
                                    v-model="type_filter"
                                    :items="question_types"
                                    chips
                                    label="Type"
                                    multiple
                                >
                                    <template v-slot:selection="{ item, index }">
                                        <v-chip v-if="index === 0">
                                            <span>{{ item }}</span>
                                        </v-chip>
                                        <span
                                            v-if="index === 1"
                                            class="grey--text caption"
                                        >(+{{ type_filter.length - 1}} others)</span>
                                    </template>
                                </v-select>
                                <span class="grey--text caption">Level</span>
                                <v-row>
                                    <v-col>
                                        <v-select
                                            v-model="level_min_filter"
                                            :items="[1, 2, 3, 4, 5]"
                                            label="Low Bound"
                                            outlined
                                        ></v-select>
                                    </v-col>
                                    <v-col>
                                        <v-select
                                            v-model="level_max_filter"
                                            :items="[1, 2, 3, 4, 5]"
                                            label="Up Bound"
                                            outlined
                                        ></v-select>
                                    </v-col>
                                </v-row>
                            </v-container>
                        </v-sheet>
                    </v-menu>
                    <v-menu offset-y transition="slide-y-transition">
                        <template v-slot:activator="{ on }">
                            <v-btn icon v-on="on">
                                <v-icon>mdi-sort</v-icon>
                            </v-btn>
                        </template>
                        <v-list>
                            <v-list-item
                                v-for="(item, index) in sort_menu"
                                :key="index"
                            >
                                <v-list-item-title>{{ item }}</v-list-item-title>
                            </v-list-item>
                        </v-list>
                    </v-menu>
                    <v-btn
                        v-if="editable && $vuetify.breakpoint.mdAndUp"
                        color="primary"
                        elevation="0"
                    >Create</v-btn>
                    <v-btn
                        v-if="editable && !$vuetify.breakpoint.mdAndUp"
                        color="primary"
                        elevation="0"
                    >
                        <v-icon>mdi-plus</v-icon>
                    </v-btn>
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
        editable: Boolean,
        id: Number,
    },
    components: {
        "tree-view": tree_view,
        "question-list-item": question_list_item
    },
    data: function() {
        return {
            type_filter: [],
            level_min_filter: 0,
            level_max_filter: 5,
            drawer: null,
            question_list: [],
            sort_menu: [
                "Popularity",
                "Level"
            ],
            keyword: "",
            question_types: [
                "Single",
                "Multiple",
                "T/F",
                "Blank Filling",
                "Brief Answer"
            ]
        }
    },
    mounted() {
        /*
        let question_1 = {
            id: 1,
            parents_node: [0, 1],
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
        */
        this.$axios
            .get("/api/question_banks/" + this.id + "/")
            .then((response) => {
                this.question_list = response.data.questions;
            })
            .catch((error) => {
                console.log(error);
            })
    },
    methods: {
        reset_filter() {
            this.type_filter = [];
            this.level_min_filter = 0;
            this.level_max_fileter = 5;
        }
    }
}
</script>