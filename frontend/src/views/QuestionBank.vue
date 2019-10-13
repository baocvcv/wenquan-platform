<template>
<div id="question-bank">
    <h1>Question Bank</h1>
    <v-card>
        <v-card-title>Profile        
            <v-btn
                absolute
                right
                text
            >Edit<v-icon>mdi-pencil</v-icon></v-btn>
        </v-card-title>
        <v-card-text>
            <span>Brief</span>
            <v-textarea
            ></v-textarea>
        </v-card-text>
    </v-card>
    <v-card>
        <v-card-title>Question List</v-card-title>
        <v-navigation-drawer
            v-model="drawer"
            clipped
            absolute
        >
            <tree-view></tree-view>
        </v-navigation-drawer>
        <v-app-bar flat clipped-left>
            <v-app-bar-nav-icon @click.stop="drawer = !drawer" class="hideen-md-and-up"></v-app-bar-nav-icon>
            <div class="v-flex-grow-1"></div>
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
        </v-app-bar>
        <v-card-text>
            <v-sheet height="500px"></v-sheet>
        </v-card-text>
    </v-card>
</div>
</template>

<script>
import tree_view from "@/components/TreeView.vue";

export default {
    name: "question-bank",
    components: {
        "tree-view": tree_view
    },
    data: () => ({
        drawer: null
    })
}
</script>