<template>
    <div id="question-list">
        <v-card app>
            <v-card-title>Question List</v-card-title>
            <v-app-bar flat clipped-left>
                <v-app-bar-nav-icon v-if="!$vuetify.breakpoint.lgAndUp" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
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
                <v-sheet height="500px">
                    <v-navigation-drawer
                        v-model="drawer"
                        overflow
                    >
                        <tree-view></tree-view>
                    </v-navigation-drawer>
                </v-sheet>
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
        drawer: null
    })
}
</script>