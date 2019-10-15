<template>
    <div id="question-list">
        <v-card app>
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
                        :cols="drawer ? 6 : 12"
                        :md="drawer ? 8 : 12"
                        :xs="12"
                    >
                        <v-card>
                            <v-card-title>This is a Title</v-card-title>
                            <v-card-text>This is the text.</v-card-text>
                        </v-card>
                    </v-col>
                </v-row>
            </v-card-text>
        </v-card>
    </div>
</template>

<script>
import tree_view from "@/components/TreeView.vue";

export default {
    name: "question-list",
    props: {
        editable: Boolean
    },
    components: {
        "tree-view": tree_view
    },
    data: () => ({
        drawer: null,
        question_list: []
    }),
    mounted() {
        question_list.push();
    }
}
</script>